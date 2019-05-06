class Calculation:

    

    def __init__(self):

        pass

    def bmi(self,weight, heigh):

        self.weight = weight

        self.heigh = heigh

        ws = "Your weight status"

        bmi_res = round(weight / ( (heigh/100) ** 2 ),1)

        if bmi_res < 18.5:

            return str("{} is underweight. \nYour BMI index is {} points.".format(ws,bmi_res))

        elif bmi_res > 18.5 and bmi_res < 24.9:

            return str("{} is normal. \nYour BMI index is {} points.".format(ws,bmi_res))

        elif bmi_res > 25 and bmi_res < 29.9:

            return str("{} is overweight. \nYour BMI index is {} points.".format(ws,bmi_res))

        else:

            return str("{} is obese. \nYour BMI index is {} points.".format(ws,bmi_res))

        

    def whr(self,waist, hip, gender):

        self.waist = waist

        self.hip = hip

        self.gender = gender

        ws = "Waist-to-Hip Ratio"

        whr_res = round(waist / hip,1)

        if gender == "male":

            if whr_res < 0.95:

                return str("{} : Low healt risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

            elif whr_res > 0.96 and whr_res < 1:

                return str("{} : Moderate risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

            else:

                return str("{} : High risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

        else:

            if whr_res < 0.80:

                return str("{} : Low healt risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

            elif whr_res > 0.81 and whr_res < 0.84:

                return str("{} : Moderate risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

            else:

                return str("{} : High risk. \nYour Waist-to-Hip Ratio index is {} points".format(ws,whr_res))

       