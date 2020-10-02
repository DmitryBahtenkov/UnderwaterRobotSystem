class GPIO:
    #time - время, в течении которого робот едет
    def Forward(self, time):
        if (time == 0):
            return "Робот едет вперёд без остановки"
        else:
            return f"Робот едет вперёд в течении {time} милисекунд"

    def Backward(self, time):
        if (time == 0):
            return "Робот едет назад без остановки"
        else:
            return f"Робот едет вперёд в течении {time} милисекунд"
    
    #angle - угол поворота
    def Left(self, angle):
        if (angle == 0):
            return "Робот бесконечно поворачивает влево"
        else:
            return f"Робот поворачивает влево на {angle} градусов"

    def Right(self, angle):
        if (angle == 0):
            return "Робот бесконечно поворачивает вправо"
        else:
            return f"Робот поворачивает вправо на {angle} градусов"

    def Stop(self):
        return "Робот стоит"

        