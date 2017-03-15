from banzai.smart import smart_instance


class RSObject:
    def __init__(self, ref):
        self.ref = ref

    def __del__(self):
        if not smart_instance.is_null(self.ref) and self.ref > 0:
            smart_instance.free_object(self.ref)
