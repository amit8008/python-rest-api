from rest_framework import serializers
from watchlist_app.models import Shows, StreamPlatform


class ShowsSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Shows
        fields = '__all__'


class StreamPlatformSerializers(serializers.ModelSerializer) :
    # All_Shows = ShowsSerializers(many = True, read_only = True)
    All_Shows = serializers.StringRelatedField(many=True)

    class Meta :
        model = StreamPlatform
        fields = '__all__'

    #     # fields = ['id', 'name', 'description']
    #     # exclude = ['active']
    #
    # def get_name_len(self, object):
    #     return len(object.name)
    #
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Movie name should not same as description")
    #     return data

# def length_gt_4(value):
#     if len(value) < 4:
#         raise serializers.ValidationError("Please provide proper movie description !")
#
#
# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators = [length_gt_4])
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # Field-level validation
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Name is too short")
#         return value
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Movie name should not same as description")
#         return data
