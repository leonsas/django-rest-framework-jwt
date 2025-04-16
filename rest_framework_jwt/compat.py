import rest_framework
from packaging.version import Version


if Version(rest_framework.VERSION) < Version('3.0.0'):
    from rest_framework.serializers import Serializer
else:
    class Serializer(rest_framework.serializers.Serializer):
        @property
        def object(self):
            return self.validated_data
