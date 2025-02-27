from fastapi import APIRouter
from typing import Any, Callable
from .message_gateway_context import MessageGatewayContext


class BaseConnector:

    def name(self) -> str:
        raise NotImplementedError

    def get_router(self) -> APIRouter:
        raise NotImplementedError

    def startup(self, context: MessageGatewayContext):
        raise NotImplementedError

    def shutdown(self, context: MessageGatewayContext):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def resume(self):
        raise NotImplementedError

    def set_gateway(self, gateway):
        raise NotImplementedError

    async def send_text_message(self, lead, text: str, metadata: dict = {}, is_partial: bool = True):
        raise NotImplementedError
    
    async def send_typing_action(self, lead):
        raise NotImplementedError
    
    async def send_message(self, message):
        raise NotImplementedError