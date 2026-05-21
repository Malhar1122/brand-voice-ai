from rich import print

from app.researcher_agent import research_topic
from app.copywriter_agent import generate_posts
from app.utils import save_output


voices = [
    "corporate",
    "startup_founder",
    "minimalist",
    "genz",
    "luxury_brand",
    "tech_influencer"
]


def main():

    print("\n[bold cyan]=== BrandVoice AI ===[/bold cyan]\n")

    topic = input("Enter topic: ").strip()

    if not topic:

        print("[red]Topic cannot be empty.[/red]")

        return

    print("\nAvailable Brand Voices:\n")

    for i, voice in enumerate(voices, start=1):

        print(f"{i}. {voice}")

    voice_input = input(
        "\nSelect voice number: "
    ).strip()

    if not voice_input:

        print("[red]Voice selection cannot be empty.[/red]")

        return

    if not voice_input.isdigit():

        print("[red]Please enter a valid number.[/red]")

        return

    choice = int(voice_input)

    if choice < 1 or choice > len(voices):

        print("[red]Invalid choice.[/red]")

        return

    selected_voice = voices[choice - 1]

    try:

        print("\n[cyan]Researching live news...[/cyan]")

        summary = research_topic(topic)

        if (
            "Unable to fetch live news" in summary
            or
            "failed" in summary.lower()
        ):

            print(
                "\n[bold red]Research Agent Failed.[/bold red]"
            )

            print(
                "[red]Unable to fetch reliable live news.[/red]"
            )

            return

        print("\n[green]Research complete.[/green]")

        print("\n[cyan]Generating social posts...[/cyan]")

        result = generate_posts(
            summary,
            selected_voice
        )

        linkedin_part = ""
        twitter_part = ""

        if "TWITTER POST:" in result:

            parts = result.split(
                "TWITTER POST:"
            )

            linkedin_part = (
                parts[0]
                .replace("LINKEDIN POST:", "")
                .strip()
            )

            twitter_part = (
                parts[1]
                .replace("X/", "")
                .replace("X:", "")
                .replace("Twitter:", "")
                .strip()
            )

        else:

            linkedin_part = result.strip()

            twitter_part = (
                "Twitter post unavailable."
            )

        print(
            "\n[bold blue]=== LINKEDIN POST ===[/bold blue]\n"
        )

        print(linkedin_part)

        print(
            "\n[bold magenta]=== TWITTER POST ===[/bold magenta]\n"
        )

        print(twitter_part)

        data = {
            "topic": topic,
            "voice": selected_voice,
            "summary": summary,
            "linkedin_post": linkedin_part,
            "twitter_post": twitter_part
        }

        file_path = save_output(
            data,
            f"{selected_voice}_output"
        )

        print(
            f"\n[green]Saved to {file_path}[/green]"
        )

    except Exception as e:

        print(
            f"\n[bold red]Unexpected Error:[/bold red] {str(e)}"
        )


if __name__ == "__main__":

    main()