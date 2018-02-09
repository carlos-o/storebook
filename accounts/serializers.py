import serpy
from storebook.settings import MEDIA_URL, URL


class CountrySerializers(serpy.Serializer):
    id = serpy.Field()
    name = serpy.Field()


class UserSerializers(serpy.Serializer):
    id = serpy.Field()
    username = serpy.Field()
    first_name = serpy.Field()
    last_name = serpy.Field()
    dni = serpy.Field()
    direction = serpy.Field()
    phone = serpy.Field()
    image = serpy.MethodField()
    country = serpy.MethodField()

    def get_country(self, obj):
        country = CountrySerializers(obj.country)
        return country

    def get_image(self, obj):
        if not obj.image:
            return (str(obj.image))
        return (URL + MEDIA_URL + str(obj.image))