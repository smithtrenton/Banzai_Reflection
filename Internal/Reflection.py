"""
*   Reflection.py contains all reflection wrappers to be used in library
*
*   RefClasses should be used with context managers always
*
*   Other wrappers only used within context manager classes
"""
import Internal.Smart as Smart
import Misc.SmartHelpers as Sh


class RefObject:
    def __init__(self, reference, hook):
        self.reference = reference
        self.field = hook[0]

    def __enter__(self):
        self.reference = Smart.smart_instance.get_field_object(
            Smart.smart_instance.target, self.reference, self.field)
        return self

    def __exit__(self, type, value, traceback):
        Smart.smart_instance.free_object(Smart.smart_instance.target, self.reference)


class RefObjectArray:
    def __init__(self, hook, index):
        self.field = hook[0]
        self.index = index

    def __enter__(self):
        self.object = Smart.smart_instance.get_field_array_object(
            Smart.smart_instance.target, 0, self.field, self.index)
        return self

    def __exit__(self, type, value, traceback):
        Smart.smart_instance.free_object(Smart.smart_instance.target, self.object)


def get_object(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldObject(Smart.smart_instance.target, reference, hook[0])


def is_hook_valid(reference, hook):
    return Smart.smart_instance.smart.exp_ishookValid(Smart.smart_instance.target, reference, hook[0])


def get_boolean(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldBoolean(Smart.smart_instance.target, reference, hook[0])


def get_long_h(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldLongH(Smart.smart_instance.target, reference, hook[0])


def get_field_long_l(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldLongL(Smart.smart_instance.target, reference, hook[0])


def get_int(reference, hook):
    return Sh.get_overflow(Smart.smart_instance.get_field_int(Smart.smart_instance.target, reference, hook[0])
                           * hook[1])


def get_short(reference, hook):

    return Smart.smart_instance.smart.exp_getFieldShort(Smart.smart_instance.target, reference, hook[0])


def get_float(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldFloat(Smart.smart_instance.target, reference, hook[0])


def get_double(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldDouble(Smart.smart_instance.target, reference, hook[0])


def get_byte(reference, hook):
    return Smart.smart_instance.smart.exp_getFieldByte(Smart.smart_instance.target, reference, hook[0])


def get_array_3d_object(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_object(Smart.smart_instance.target,
                                                          reference, hook[0], x, y, z)


def get__array_3d_char(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_char(reference, hook[0], x, y, z)


def get_array_3d_short(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_short(reference, hook[0], x, y, z)


def get_array_3d_int(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_int(reference, hook[0], x, y, z)


def get_array_3d_float(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_float(reference, hook[0], x, y, z)


def get_array_3d_double(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_double(reference, hook[0], x, y, z)


def get_array_3d_bool(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_bool(reference, hook[0], x, y, z)


def get_array_3d_long_h(reference, hook, x, y, z):
    return Smart.smart_instance.get_field_array_3d_long_h(reference, hook[0], x, y, z)


def get_3d_long_l(reference, hook, x, y, z):
    return Smart.smart_instance.get_array_3d_long_l(reference, hook[0], x, y, z)


def get_array_2d_object(reference, hook, x, y):
    return Smart.smart_instance.get_array_2d_object(reference, hook[0], x, y)


def get_array_2d_int(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DInt(Smart.smart_instance.target, reference,
                                                             Sh.string_to_char_p(hook[0]), x, y)


def get_array_2d_double(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DDouble(Smart.smart_instance.target, reference,
                                                                Sh.string_to_char_p(hook[0]), x, y)


def get_array_2d_float(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DFloat(Smart.smart_instance.target, reference,
                                                               Sh.string_to_char_p(hook[0]), x, y)


def get_array_2d_bool(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DBool(Smart.smart_instance.target, reference,
                                                              Sh.string_to_char_p(hook[0]), x, y)


def get_array_2d_long_h(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DLongH(Smart.smart_instance.target, reference, hook[0], x, y)


def get_array_2d_long_l(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DLongL(Smart.smart_instance.target, reference, hook[0], x, y)


def get_array_2d_byte(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DByte(Smart.smart_instance.target, reference, hook[0], x, y)


def get_array_2d_char(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DChar(Smart.smart_instance.target, reference, hook[0], x, y)


def get_array_2d_short(reference, hook, x, y):
    return Smart.smart_instance.smart.exp_getFieldArray2DShort(Smart.smart_instance.target, reference, hook[0], x, y)


def get_array_size(reference, hook, dimension):
    return Smart.smart_instance.smart.exp_getFieldArraySize(Smart.smart_instance.target, reference, hook[0], dimension)


def get_object_array(reference, hook, index):
    return Smart.smart_instance.get_field_array_object(Smart.smart_instance.target, reference, hook[0], index)


def get_int_array(reference, hook, index):
    return Smart.smart_instance.get_field_array_int(Smart.smart_instance.target, reference, hook[0], index)


def get_array_float(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayFloat(Smart.smart_instance.target, reference, hook[0], index)


def get_array_double(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayDouble(Smart.smart_instance.target, reference, hook[0], index)


def get_array_bool(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayBool(Smart.smart_instance.target, reference, hook[0], index)


def get_array_long_h(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayLongH(Smart.smart_instance.target, reference, hook[0], index)


def get_array_long_l(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayLongL(Smart.smart_instance.target, reference, hook[0], index)


def get_array_byte(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayByte(Smart.smart_instance.target, reference, hook[0], index)


def get_array_short(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayShort(Smart.smart_instance.target, reference, hook[0], index)


def get_array_char(reference, hook, index):
    return Smart.smart_instance.smart.exp_getFieldArrayChar(Smart.smart_instance.target, reference, hook[0], index)


def free_object(reference):
    Smart.smart_instance.smart.exp_freeObject(Smart.smart_instance.target, reference)


def string_from_string(reference, strng):
    return Smart.smart_instance.smart.exp_stringFromString(
        Smart.smart_instance.target, reference, Sh.string_to_char_p(strng))


def string_from_chars(reference, strng):
    return Smart.smart_instance.smart.exp_stringFromChars(
        Smart.smart_instance.target, reference, Sh.string_to_char_p(strng))


def string_from_bytes(reference, strng):
    return Smart.smart_instance.smart.exp_stringFromBytes(
        Smart.smart_instance.target, reference, Sh.string_to_char_p(strng))


def get_string(reference, hook):
    with get_object(reference, hook) as str_int:
        temp = string_from_string(str_int, 512)
        temp = temp.replace('Â', '')
        temp = temp.replace('#160', '#32')
        return temp


def is_null(reference):
    return Smart.smart_instance.smart.exp_isNull(Smart.smart_instance.target, reference)


def is_equal(reference):
    return Smart.smart_instance.smart.exp_isEqual(Smart.smart_instance.target, reference)
