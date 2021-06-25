# <pep8-80 compliant>
import time


# Class
class EvaluateTime():
    """Evaluate time of script execution"""

    # Class execution 1
    def init(t_time):
        init_time_counter(t_time)
        return {'FINISHED'}

    # Class execution 2
    def evaluate_time(t_time_started):
        evaluate_time(t_time_started)
        return {'FINISHED'}


def init_time_counter(t_time_start):
    t_time_start = time.time()


def evaluate_time(t_time_started):
    print("Script terminado em: %.4f sec" % (time.time() - t_time_started))


# To register
def register():
    bpy.utils.register_class(EvaluateTime)


# To unregister
def unregister():
    bpy.utils.unregister_class(EvaluateTime)


# Register
if __name__ == "__main__":
    register()
