from office365.runtime.client_object_collection import ClientObjectCollection
from office365.runtime.client_query import ClientQuery
from office365.runtime.resource_path_service_operation import ResourcePathServiceOperation
from office365.sharepoint.field import Field


class FieldCollection(ClientObjectCollection):
    """Represents a collection of Field resource."""

    def __init__(self, context, resource_path=None):
        super(FieldCollection, self).__init__(context, Field, resource_path)

    def add(self, field_creation_information):
        """Adds a field to the field collection."""
        field = Field(self.context)
        qry = ClientQuery.create_entry_query(self, field_creation_information)
        self.context.add_query(qry, field)
        self.add_child(field)
        return field

    def get_by_id(self, _id):
        """Gets the field with the specified ID."""
        return Field(self.context, ResourcePathServiceOperation(self.context, self.resource_path, "getById", [_id]))

    def get_by_internal_name_or_title(self, name_title):
        """Returns the first Field object with the specified internal name or title from the collection."""
        return Field(self.context,
                     ResourcePathServiceOperation(self.context,
                                                  self.resource_path,
                                                  "getByInternalNameOrTitle", [name_title]))

    def get_by_title(self, title):
        """Returns the first field object in the collection based on the title of the specified field."""
        return Field(self.context,
                     ResourcePathServiceOperation(self.context, self.resource_path, "getByTitle", [title]))
