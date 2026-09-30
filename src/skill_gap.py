# ============================================================
# CareerFuture AI - Skill Gap Engine
# ============================================================

# Required skill levels for each role.
# Scale:
# 0 = No knowledge
# 1 = Beginner
# 2 = Basic
# 3 = Intermediate
# 4 = Advanced
# 5 = Strong

ROLE_REQUIREMENTS = {

    # --------------------------------------------------------
    # ML ENGINEER
    # --------------------------------------------------------

    "ML Engineer": {

        "python": 4,

        "sql": 4,

        "machine_learning": 4,

        "deep_learning": 3,

        "statistics": 4,

        "data_preprocessing": 4,

        "model_evaluation": 4,

        "docker": 3,

        "cloud": 3,

        "pytorch": 3,

        "projects": 5
    },


    # --------------------------------------------------------
    # DATA SCIENTIST
    # --------------------------------------------------------

    "Data Scientist": {

        "python": 4,

        "sql": 4,

        "machine_learning": 4,

        "deep_learning": 2,

        "statistics": 5,

        "data_preprocessing": 4,

        "model_evaluation": 4,

        "nlp": 2,

        "projects": 5
    },


    # --------------------------------------------------------
    # DATA ANALYST
    # --------------------------------------------------------

    "Data Analyst": {

        "python": 3,

        "sql": 5,

        "statistics": 4,

        "data_preprocessing": 4,

        "model_evaluation": 3,

        "projects": 4
    },


    # --------------------------------------------------------
    # BACKEND DEVELOPER
    # --------------------------------------------------------

    "Backend Developer": {

        "java": 4,

        "spring_boot": 4,

        "sql": 4,

        "dsa": 4,

        "docker": 3,

        "nodejs": 3,

        "projects": 5
    },


    # --------------------------------------------------------
    # AI ENGINEER
    # --------------------------------------------------------

    "AI Engineer": {

        "python": 5,

        "machine_learning": 4,

        "deep_learning": 4,

        "nlp": 4,

        "pytorch": 4,

        "tensorflow": 3,

        "docker": 3,

        "cloud": 3,

        "projects": 5
    },


    # --------------------------------------------------------
    # DEVOPS ENGINEER
    # --------------------------------------------------------

    "DevOps Engineer": {

        "linux": 4,

        "docker": 4,

        "kubernetes": 4,

        "cloud": 4,

        "aws": 4,

        "dsa": 3,

        "projects": 5
    }
}


# ============================================================
# CALCULATE SKILL GAPS
# ============================================================

def calculate_skill_gaps(
    candidate: dict,
    role: str
):

    # Check whether requested role exists

    if role not in ROLE_REQUIREMENTS:

        raise ValueError(
            f"Unknown role: {role}"
        )


    requirements = ROLE_REQUIREMENTS[
        role
    ]


    gaps = {}


    # --------------------------------------------------------
    # Compare candidate level with required level
    # --------------------------------------------------------

    for skill, required_level in requirements.items():

        # If the skill isn't provided,
        # assume candidate level = 0

        current_level = candidate.get(
            skill,
            0
        )


        # If current level is below
        # required level, there is a gap

        if current_level < required_level:

            gaps[skill] = {

                "current": current_level,

                "required": required_level,

                "gap": (
                    required_level -
                    current_level
                )
            }


    return gaps


# ============================================================
# CALCULATE SKILL MATCH PERCENTAGE
# ============================================================

def calculate_skill_match(
    candidate: dict,
    role: str
):

    if role not in ROLE_REQUIREMENTS:

        raise ValueError(
            f"Unknown role: {role}"
        )


    requirements = ROLE_REQUIREMENTS[
        role
    ]


    total_required = 0
    total_achieved = 0


    for skill, required_level in requirements.items():

        current_level = candidate.get(
            skill,
            0
        )


        # A candidate cannot get more
        # than the required amount for
        # the matching calculation.

        achieved = min(
            current_level,
            required_level
        )


        total_required += required_level

        total_achieved += achieved


    if total_required == 0:

        return 0.0


    match_percentage = (
        total_achieved /
        total_required
    ) * 100


    return round(
        match_percentage,
        2
    )


# ============================================================
# GENERATE COMPLETE ROLE ANALYSIS
# ============================================================

def analyze_role(
    candidate: dict,
    role: str
):

    gaps = calculate_skill_gaps(
        candidate,
        role
    )


    match_percentage = (
        calculate_skill_match(
            candidate,
            role
        )
    )


    return {

        "role": role,

        "skill_match_percentage":
            match_percentage,

        "number_of_gaps":
            len(gaps),

        "skill_gaps":
            gaps
    }