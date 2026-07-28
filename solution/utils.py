def validate_input(data):

    required=[

        "vin",

        "vout",

        "load_current",

        "output_ripple",

        "inductor_ripple"

    ]

    for k in required:

        if k not in data:

            raise ValueError(f"Missing {k}")