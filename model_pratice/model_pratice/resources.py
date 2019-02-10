from import_export import resources

from home.models import Medical_library


class Medical_libraryResource(resources.ModelResource):
    class Meta:
        model = Medical_library
