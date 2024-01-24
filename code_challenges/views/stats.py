import reflex as rx
import code_challenges.styles.styles as styles
from code_challenges.routes import Route
from code_challenges.data.Stats import Stats, LanguageRanking, ChallengeRanking, UserRanking
from code_challenges.styles.styles import Size, TextColor
from code_challenges.components.milestone import milestone, Milestone
from code_challenges.components.button import button


def stats(stats: Stats) -> rx.Component:
    return rx.vstack(
        # rx.link(
        rx.stack(
            milestone(
                stats.languages_total,
                "Lenguajes",
                _languages(stats.languages_ranking),
                TextColor.YELLOW
            ),
            milestone(
                stats.files_total,
                "Contribuciones",
                _challenges(stats.challenges_ranking),
                TextColor.GREEN
            ),
            milestone(
                stats.users_total,
                "Usuarios",
                _users(stats.users_ranking),
                TextColor.PINK
            ),
            spacing=Size.BIG.value,
            width="100%",
            direction=styles.STACK_DIRECTION
        ),
        # href=Route.ROADMAP_RANKING.value,
        # ),
        # button(
        #     "Ver el ranking completo",
        #     Route.ROADMAP_RANKING.value,
        #     is_external=False
        # ),
        spacing=Size.BIG.value,
        style=styles.max_width_style
    )


def _languages(languages: [LanguageRanking]) -> [Milestone]:
    milestones = []
    for index in range(5):
        language = languages[index]
        milestones.append(
            Milestone(
                f"devicon-{language.name}-plain",
                f"{language.name} ({language.count})",
                True
            )
        )
    return milestones


def _challenges(challenges: [ChallengeRanking]) -> [Milestone]:
    milestones = []
    for index in range(5):
        challenge = challenges[index]
        milestones.append(
            Milestone(
                "/icons/star.svg",
                f"#{challenge.name.split(' - ')[0]} ({challenge.count})"
            )
        )
    return milestones


def _users(users: [UserRanking]) -> [Milestone]:
    milestones = []
    for index in range(5):
        user = users[index]
        milestones.append(
            Milestone(
                "/icons/trophy.svg",
                f"#{user.order} {user.name} ({user.count})"
            )
        )
    return milestones
