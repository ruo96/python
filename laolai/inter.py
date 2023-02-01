import time
from typing import List

import openmined_psi as psi
import syft as sy
from syft import DomainClient
from syft.core.node.common.node_service.auth import AuthorizationException
from syft.core.pointer.pointer import Pointer


def wait_store_item(domain: DomainClient, condition: str) -> Pointer:
    ls = []
    while True:
        ls = [x for x in domain.store.store if condition in x.tags]
        if len(ls) == 0:
            time.sleep(1)
        else:
            break
    return ls[0]


def get_remote(try_seconds: int, reason: str, pointer: Pointer):
    pointer.request(reason=reason)
    msg = None
    for i in range(try_seconds):
        try:
            msg = pointer.get(
                delete_obj=False
            )
            break;
        except AuthorizationException:
            i = i + 1
            time.sleep(1)
    if msg is None:
        raise Exception("没有获取到setup的值")
    return msg


class PsiClient:
    def __init__(self, session: str, domain: DomainClient, reveal_intersection: bool, client_items: List[str]):
        self.session = session
        self.domain = domain
        self.setup_info = None
        self.reveal_intersection = reveal_intersection
        self.client = psi.client.CreateWithNewKey(reveal_intersection)
        self.client_items = client_items

    def setup(self):
        # 1. 首先客户端提供 client_items_len
        print("1. 首先客户端提供 client_items_len")
        sy.lib.python.Int(len(self.client_items)).send(
            self.domain,
            pointable=True,
            tags=[f"{self.session}client_items_len"],
            description=f"{self.session}: 求交初始化: fpr=1e-6, reveal_intersection={self.reveal_intersection}"
        )
        # 2. 等待服务端 setup
        print("2. 等待服务端 setup")
        setup_ptr = wait_store_item(self.domain, f'{self.session}setup')
        # 3. 获取 setup 的值
        print("3. 获取 setup 的值")
        setup_msg = get_remote(30, f"{self.session}: 需要setup", setup_ptr)
        setup = psi.ServerSetup()
        setup.ParseFromString(setup_msg[0])
        self.setup_info = setup

    def intersect(self) -> (int, List[str]):
        # 1. 客户端发送 request
        print("1. 客户端发送 request")
        request = self.client.CreateRequest(self.client_items)
        msg = request.SerializeToString()
        wrapper = sy.lib.python.List()
        wrapper.append(msg)
        wrapper.send(
            self.domain,
            tags=[f"{self.session}request"],
            pointable=True,
            description=f"{self.session}: 求交request"
        )
        # 2. 等待服务端返回 response
        print("2. 等待服务端返回 response")
        response_ptr = wait_store_item(self.domain, f"{self.session}response")
        # 3. 获取 response
        print("3. 获取 response")
        rep_msg = get_remote(30, f"{self.session}: 需要response", response_ptr)
        response = psi.Response()
        response.ParseFromString(rep_msg[0])
        # 4. 计算 intersection
        print("4. 计算 intersection")
        if self.reveal_intersection:
            intersection = self.client.GetIntersection(self.setup_info, response)
            intersected_items = [item for index, item in enumerate(self.client_items) if index in set(intersection)]
            return len(intersected_items), intersected_items
        else:
            return self.client.GetIntersectionSize(self.setup_info, response), None


class PsiServer:
    def __init__(self, session: str, domain: DomainClient, reveal_intersection: bool, server_items: List[str]):
        self.session = session
        self.domain = domain
        self.reveal_intersection = reveal_intersection
        self.server = psi.server.CreateWithNewKey(reveal_intersection)
        self.server_items = server_items

    def setup(self):
        # 1. 等待客户端发送 client_items_len
        print("1. 等待客户端发送 client_items_len")
        client_items_len_ptr = wait_store_item(self.domain, f"{self.session}client_items_len")
        # 2. 服务端获取 client_items_len
        print("2. 服务端获取 client_items_len")
        client_items_len = self.get_local(client_items_len_ptr)
        # 3. 服务端创建 setup
        print("3. 服务端创建 setup")
        setup = self.server.CreateSetupMessage(1e-6, client_items_len, self.server_items)
        setup_msg = setup.SerializeToString()
        wrapper = sy.lib.python.List()
        wrapper.append(setup_msg)
        wrapper.send(self.domain, pointable=True, tags=[f"{self.session}setup"], description=f"{self.session}: 设置好了")
        # 4. 同意客户端获取 setup
        print("4. 同意客户端获取 setup")
        time.sleep(3)
        self.accept(f"{self.session}: 需要setup")

    def process_request(self):
        # 1. 等待客户端发起 request
        print("1. 等待客户端发起 request")
        request_ptr = wait_store_item(self.domain, f"{self.session}request")
        # 2. 服务端获取 request
        print("2. 服务端获取 request")
        msg = self.get_local(request_ptr)
        request = psi.Request()
        request.ParseFromString(msg[0])
        # 3. 处理 request
        print("3. 处理 request")
        response = self.server.ProcessRequest(request)
        rep_msg = response.SerializeToString()
        wrapper = sy.lib.python.List()
        wrapper.append(rep_msg)
        wrapper.send(self.domain, pointable=True, tags=[f"{self.session}response"], description="求交结果计算好了")
        # 4. 同意客户端获取 response
        print("4. 同意客户端获取 response")
        time.sleep(3)
        self.accept(f"{self.session}: 需要response")

    def accept(self, reason: str):
        [x for x in self.domain.requests.requests if x.request_description == reason][0].accept()

    def get_local(self, pointer: Pointer):
        reason = f"{self.session}: 获取{pointer.tags}"
        pointer.request(reason=reason)
        time.sleep(1)
        self.accept(reason)
        time.sleep(1)
        v = pointer.get(
            delete_obj=False
        )
        return v
