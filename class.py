#we're going to learn about classes. YIPPEE
#first unpack the list that is returned as a result of the controller intake
#following this unpacking we can pass the parameters into the


class My_ROV:
    def __init__(self, left_x_input, right_x_input, left_y_input, right_y_input):
        self.left_x = left_x_input
        self.right_x = right_x_input
        self.left_y = left_y_input
        self.right_y = right_y_input

    def movement(self):
        #if all vall = 0 leave
        #else keep assessing
        if self.left_y + self.left_x + self.right_y + self.right_x != 0:
            #set list x for processed inputs x and break
        else:
            #continue





