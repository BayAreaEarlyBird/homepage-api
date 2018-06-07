# class ViewerCanUpdate(graphene.Field):
#     @staticmethod
#     def viewer_can_update_resolver(parent_resolver, root, info, **args):
#         viewer = args.get('viewer')
#
#         return True
#
#     def get_resolver(self, parent_resolver):
#         return partial(
#             self.id_resolver, parent_resolver
#         )
#
#
# class Updatable(graphene.Interface):
#     @classmethod
#     def __init_subclass_with_meta__(cls, **options):
#         _meta = InterfaceOptions(cls)
#         _meta.fields = OrderedDict(
#             viewer_can_update=ViewerCanUpdate(
#                 default=True,
#                 required=True,
#                 description='Whether the viewer can update the object.')
#         )
#         super(Updatable, cls).__init_subclass_with_meta__(
#             _meta=_meta, **options)
