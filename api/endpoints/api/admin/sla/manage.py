from sanic import Request, json
from sanic.views import HTTPMethodView


class SLAManage(HTTPMethodView):
    # TODO
    async def get(self, request: Request):
        return json({"error": "Not implemented"}, status=501)
