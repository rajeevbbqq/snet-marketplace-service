from registry.infrastructure.repositories.service_repository import ServiceRepository

ALLOWED_ATTRIBUTES_FOR_SERVICE_SEARCH = ["display_name"]
DEFAULT_ATTRIBUTE_FOR_SERVICE_SEARCH = "display_name"
ALLOWED_ATTRIBUTES_FOR_SERVICE_SORT_BY = ["ranking", "service_id"]
DEFAULT_ATTRIBUTES_FOR_SERVICE_SORT_BY = "ranking"
ALLOWED_ATTRIBUTES_FOR_SERVICE_ORDER_BY = ["asc", "desc"]
DEFAULT_ATTRIBUTES_FOR_SERVICE_ORDER_BY = "desc"
DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 0


class ServicePublisherService:
    def __init__(self, username, org_uuid, service_uuid):
        self.username = username
        self.org_uuid = org_uuid
        self.service_uuid = service_uuid

    def verify_service_id(self, service_id):
        pass

    def save_service(self, payload):
        pass

    def create_service(self, payload):
        pass

    def get_services_for_organization(self, payload):
        offset = payload.get("offset", DEFAULT_OFFSET)
        limit = payload.get("limit", DEFAULT_LIMIT)
        search_string = payload["q"]
        search_attribute = payload["s"]
        sort_by = payload["sort_by"].lower()
        order_by = payload["order_by"].lower()
        filter_parameters = {
            "offset": offset,
            "limit": limit,
            "search_string": search_string,
            "search_attribute": search_attribute if search_attribute in ALLOWED_ATTRIBUTES_FOR_SERVICE_SEARCH else DEFAULT_ATTRIBUTE_FOR_SERVICE_SEARCH,
            "sort_by": sort_by if sort_by in ALLOWED_ATTRIBUTES_FOR_SERVICE_SORT_BY else DEFAULT_ATTRIBUTES_FOR_SERVICE_SORT_BY,
            "order_by": order_by if order_by in ALLOWED_ATTRIBUTES_FOR_SERVICE_SORT_BY else DEFAULT_ATTRIBUTES_FOR_SERVICE_ORDER_BY
        }
        search_result = ServiceRepository().get_services_for_organization(self.org_uuid, filter_parameters)
        search_count = ServiceRepository().get_total_count_of_services_for_organization(self.org_uuid, filter_parameters)
        return {"total_count": search_count,  "offset": offset, "limit": limit, "result": search_result}
