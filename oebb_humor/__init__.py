from otree.api import *


doc = """
ÖBB Chatbot Humor Experiment
Between-subjects: Humor style (affiliative / self-defeating / neutral)
Within-subjects: Failure severity (low / high), counterbalanced order
"""


COUNTRY_LIST = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
    "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
    "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Democratic Republic of the Congo",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia",
    "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan",
    "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg",
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
    "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "North Korea", "North Macedonia", "Norway",
    "Oman",
    "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal",
    "Qatar",
    "Romania", "Russia", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
    "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan",
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Yemen",
    "Zambia", "Zimbabwe"
]


class C(BaseConstants):
    NAME_IN_URL = 'oebb_humor'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2  # 2 scenarios per participant

    HUMOR_STYLES = ['affiliative', 'self_defeating', 'neutral']
    SEVERITIES = ['low', 'high']  # seat double booking vs train cancellation


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --- Treatment assignment (copied from participant each round) ---
    humor_style = models.StringField()
    scenario_severity = models.StringField()  # "low" (seat issue) or "high" (train cancellation)

    # --- Consent (round 1 only) ---
    consent = models.BooleanField(
        label="I am at least 18 years old, have read the information above, and agree to take part in this study."
    )

    # --- Pre-experiment context (round 1 only) ---
    booking_familiarity = models.IntegerField(
        label="How familiar are you with booking train or other travel services online?",
        choices=[
            [1, "Not at all familiar"],
            [2, "Slightly familiar"],
            [3, "Moderately familiar"],
            [4, "Very familiar"],
            [5, "Extremely familiar"],
        ],
        widget=widgets.RadioSelect,
    )

    chatbot_experience = models.IntegerField(
        label="How often have you used customer service chatbots in the past?",
        choices=[
            [1, "Never"],
            [2, "Rarely"],
            [3, "Sometimes"],
            [4, "Often"],
            [5, "Very often"],
        ],
        widget=widgets.RadioSelect,
    )

    # --- Chat log (per scenario) ---
    chat_log = models.LongStringField(blank=True)

    # --- Main DVs per scenario (7-point Likert) ---
    satisfaction = models.IntegerField(
        label="Overall, I am satisfied with how the chatbot handled this situation.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )
    competence = models.IntegerField(
        label="The chatbot seemed competent in handling this situation.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )
    warmth = models.IntegerField(
        label="The chatbot seemed warm and friendly.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )
    anthropomorphism = models.IntegerField(
        label="The chatbot felt human-like.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )
    reuse = models.IntegerField(
        label="I would use this chatbot again to solve a similar situation.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )

    attention_check_item = models.IntegerField(
        label=(
            "For this statement, please select 'Somewhat agree'."
        ),
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )

    # --- Manipulation checks per scenario ---
    severity_check = models.IntegerField(
        label="The situation felt like a serious service problem.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )
    humor_check = models.IntegerField(
        label="The chatbot’s response used humor.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelect,
    )



    # --- Demographics & general questions (shown after round 2) ---
    age = models.IntegerField(
        min=18,
        max=99,
        label="Age",
    )

    gender = models.StringField(
        choices=[
            ['female', 'Female'],
            ['male', 'Male'],
            ['nonbinary', 'Non-binary / other'],
            ['prefer_not', 'Prefer not to say'],
        ],
        label="Gender",
        blank=True,
    )

    country_origin = models.StringField(
        label="Country of origin",
        choices=[(c, c) for c in COUNTRY_LIST],
        blank=True,
    )

    train_frequency = models.StringField(
        label="How often do you usually travel by train?",
        choices=[
            ['rarely', 'Rarely (less than once per year)'],
            ['few_per_year', 'A few times per year'],
            ['monthly', 'About once per month'],
            ['weekly_plus', 'At least once per week'],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    # NOTE: here we add the labels *into the choices* so the default widget shows full anchors.
    humor_preference = models.IntegerField(
        label="In general, I like when service providers use humor in their communication.",
        choices=[
            [1, "1 – Strongly disagree"],
            [2, "2 – Disagree"],
            [3, "3 – Somewhat disagree"],
            [4, "4 – Neutral"],
            [5, "5 – Somewhat agree"],
            [6, "6 – Agree"],
            [7, "7 – Strongly agree"],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    chatbot_opinion = models.IntegerField(
        label="Overall, I have a positive opinion of automated service chatbots.",
        choices=[
            [1, "1 – Strongly disagree"],
            [2, "2 – Disagree"],
            [3, "3 – Somewhat disagree"],
            [4, "4 – Neutral"],
            [5, "5 – Somewhat agree"],
            [6, "6 – Agree"],
            [7, "7 – Strongly agree"],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    feedback = models.LongStringField(
        label="If you want, you can share any comments about this chatbot interaction or the study.",
        blank=True,
    )

    raffle_email = models.StringField(
        label="Email address (optional)",
        blank=True,
    )


# --- Treatment assignment & counterbalancing ---

def creating_session(subsession: Subsession):
    import random

    if subsession.round_number == 1:
        for p in subsession.get_players():
            # Between-subjects: assign humor style
            style = random.choice(C.HUMOR_STYLES)
            p.participant.humor_style = style

            # Within-subjects: random order of low/high severity
            order = C.SEVERITIES.copy()   # ['low', 'high']
            random.shuffle(order)         # now ['high', 'low'] or ['low', 'high']
            p.participant.scenario_order = order

            # Give the participant a reservation number (for realism)
            p.participant.reservation_number = random.randint(40000, 99999)

    # For every round, copy from participant into Player fields
    for p in subsession.get_players():
        p.humor_style = p.participant.humor_style
        order = p.participant.scenario_order
        p.scenario_severity = order[subsession.round_number - 1]


# --- Pages ---

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            info_text=(
                "You are invited to take part in a short online study about digital customer service in rail transport. "
                "You will be asked to imagine train trips with service disruptions and see responses from the ÖBB service chatbot. "
                "Your participation is anonymous and voluntary. You can stop at any time by closing the browser. "
                "Only aggregated data will be analyzed for academic purposes."
            )
        )

    @staticmethod
    def error_message(player: Player, values):
        if not values.get('consent'):
            return "To participate you need to confirm your consent."


class Intro(Page):
    form_model = 'player'
    form_fields = ['booking_familiarity', 'chatbot_experience']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            intro_text=(
                "Imagine you booked your train journey using the ÖBB app. "
                "During your trip, you need support from the ÖBB service chatbot."
            ),
            explanation=(
                "Before we show you the situations, we would like to know about your prior experience with "
                "online bookings and service chatbots."
            ),
        )


class ScenarioIntro(Page):
    @staticmethod
    def vars_for_template(player: Player):
        context = Scenario.vars_for_template(player)
        context.update(
            instructions=(
                "On the next screen, you will see a chat with the ÖBB service chatbot. "
                "First, please read the situation below carefully. Then click 'Next' to "
                "proceed to the chatbot interaction."
            )
        )
        return context


class Scenario(Page):
    form_model = 'player'
    form_fields = ['chat_log']

    @staticmethod
    def vars_for_template(player: Player):
        # Get reservation number if available
        reservation_number = getattr(player.participant, 'reservation_number', None)
        if reservation_number is None:
            reservation_number = '—'

        if player.scenario_severity == 'low':
            scenario_description = (
                "You are travelling from Vienna to Budapest. When you board your train and reach your reserved seat, "
                "you find that someone is already sitting there. It appears that the seat has been double-booked. "
                "The train seems quite full, but the ÖBB app suggests contacting the ÖBB service chatbot for help "
                "with your seating situation."
            )
            header_title = "ÖBB Assist – Seat Issue Support"
            severity_label = "Low-severity: seat double booking"
        else:
            scenario_description = (
                "You are travelling from Budapest to Vienna. Shortly before your departure, you receive a "
                "notification in the ÖBB app that your train has been cancelled due to operational issues. "
                "The next available train departs in about one hour. You contact the ÖBB service chatbot to "
                "find out how to continue your journey."
            )
            header_title = "ÖBB Assist – Train Disruption Support"
            severity_label = "High-severity: train cancellation"

        return dict(
            scenario_description=scenario_description,
            header_title=header_title,
            severity_label=severity_label,
            humor_condition=player.humor_style.replace('_', ' '),
            severity_key=player.scenario_severity,
            humor_key=player.humor_style,
            reservation_number=reservation_number,
        )




class ScenarioRatings(Page):
    form_model = 'player'
    form_fields = [
        'satisfaction',
        'competence',
        'warmth',
        'anthropomorphism',
        'reuse',
        'severity_check',
        'humor_check',
        'attention_check_item',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        if player.scenario_severity == 'low':
            severity_label = "Situation: seat double booking"
        else:
            severity_label = "Situation: train cancellation"
        return dict(severity_label=severity_label)


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'country_origin',
        'train_frequency',
        'humor_preference',
        'chatbot_opinion',
        'feedback',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        # safe access for pre-filling age & country if the page is reloaded
        age_value = player.field_maybe_none('age') or ''
        selected_country = player.field_maybe_none('country_origin') or ''
        return dict(
            country_choices=COUNTRY_LIST,
            age_value=age_value,
            selected_country=selected_country,
        )

    @staticmethod
    def error_message(player: Player, values):
        errors = {}

        age = values.get('age')
        if age is None:
            errors['age'] = "Please enter your age."
        elif age < 18 or age > 99:
            errors['age'] = "Please enter a valid age between 18 and 99."

        country = values.get('country_origin')
        if not country:
            errors['country_origin'] = "Please select your country of origin."

        if errors:
            return errors


class Debrief(Page):
    form_model = 'player'
    form_fields = ['raffle_email']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            debrief_text=(
                "Thank you for participating. This study investigates how different chatbot response styles "
                "(with and without humor) influence reactions to service disruptions in public rail transport. "
                "In particular, we compare different types of humor and different levels of disruption severity. "
                "If you have any questions or wish to withdraw your data, please contact the researcher using "
                "the information provided by your institution."
            )
        )


class Raffle(Page):
    form_model = 'player'
    form_fields = ['raffle_email']

    @staticmethod
    def is_displayed(player: Player):
        # Only after the second (last) scenario
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            raffle_text=(
                "As a thank you for taking part in this study, we will raffle a "
                "50 EUR Amazon gift card among participants. "
                "If you would like to enter the raffle, please leave your email address below. "
                "Participation in the raffle is completely optional and your entry "
                "will only be counted once. Your email address will only be used to "
                "contact you in case you win."
            )
        )


page_sequence = [
    Consent,
    Intro,
    ScenarioIntro,
    Scenario,
    ScenarioRatings,
    Demographics,
    Debrief,
    Raffle,
]

