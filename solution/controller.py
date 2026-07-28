def compensate(data,fault):

    duty=data["vout"]/data["vin"]

    if fault=="Low Inductance":
        duty*=1.01

    if fault=="High ESR Capacitor":
        duty*=0.995

    return {

        "fault":fault,

        "recommended_duty_cycle":round(duty,4)
    }