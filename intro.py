import time
from multiprocessing import Process, Value
from example_process import Example_Process
from kill_button_interface import Kill_Button_Interface
from motors.MotorWrapper import Can_Wrapper
from shared_memory_wrapper import SharedMemoryWrapper


class Intro_Class:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object

    def run_loop(self):
        # defining our motor
        motor = Can_Wrapper()
        # Looping while our shared memory object is true ->
        while self.shared_memory_object.running.value:
            # write code here
            '''
            Create a timer 
            each time we increase the timer 
            we modulo which process we wish to execute 
            and they go in their steps 
            20 - 30 -> up 
            73 - 99 -> right 
            '''
            # Saving our current time, so we know how
            # long to pause our motors for
            start = time.time()

            # Check iterations (Can't be more than 100)
            if self.shared_memory_object.iterations > 8:
                # Reset our iterations
                self.shared_memory_object.iteration = 0

            # Now we can see what to do depending on
            # What our iterations are

            # we have 8 things we are supposed to do ->
            if self.shared_memory_object.iteration == 0:
                print("Moving forward 1")
                motor.move_forward(1)
            elif self.shared_memory_object.iteration == 1:
                print(" Move left 1")
                motor.turn_left(1)
            elif self.shared_memory_object.iteration == 2:
                motor.turn_left(1)
                print(" Move backwards 1 ")
            elif self.shared_memory_object.iteration == 3:
                print("Move right 1 ")
                motor.turn_right(1)
            elif self.shared_memory_object.iteration == 4:
                print("Move up 1 ")
                motor.move_up(1)
            elif self.shared_memory_object.iteration == 5:
                print("Move down 1 ")
                motor.move_down(1)
            elif self.shared_memory_object.iteration == 6:
                print("Roll to the right")
                motor.roll_right(1)
            elif self.shared_memory_object.iteration == 7:
                print("Roll to the left")
                motor.roll_left(1)

            # Now no matter what we execute we need to let
            # our motors rest for 50 milliseconds ->
            time.sleep(.05)

            self.shared_memory_object.iteration += 1
            # forwards, strafe left, backwards, strafe right
            # end
            pass
