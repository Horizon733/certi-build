import sys
import click
from certi_builder.builder import generate_certificate, path_exist, validate_hex


@click.group()
@click.version_option("1.0.1")
def main():
    pass


@main.command()
@click.option(
    "--certificate-image-path",
    prompt=True,
    type=str,
    required=True,
    help="Certificate image path formats excepted: [png, jpg, pdf]",
)
@click.option(
    "--excel-file-path",
    prompt=True,
    type=str,
    required=True,
    help="Excel file path which consists names of people",
)
@click.option(
    "--text-color", prompt=True, type=str, required=True, help="Provide Hex color"
)
@click.option(
    "--font-file-path",
    prompt=True,
    type=str,
    required=True,
    help="We current support TrueType font",
)
@click.option("--font-size", prompt=True, type=int, required=True, help="Font size")
@click.option(
    "--output-location",
    prompt=True,
    type=str,
    required=True,
    help="a directory to store all certificates E.g D:/directory",
)
@click.option(
    "--x-location",
    prompt=True,
    type=float,
    required=True,
    help="x-axis coords for text to be placed",
)
@click.option(
    "--y-location",
    prompt=True,
    type=float,
    required=True,
    help="y-axis coords for text to be placed",
)
@click.option(
    "--bold", is_flag=True, required=False, help="if you want names to be bold."
)
def build(
    certificate_image_path,
    excel_file_path,
    text_color,
    font_file_path,
    font_size,
    x_location,
    y_location,
    output_location,
    bold,
):
    """
    Generate certificates on go. Every option will be prompted except bold
    """
    image_exists, message = path_exist(certificate_image_path, True)
    if not image_exists:
        click.echo(f"Error: {message}")
        return
    excel_exists, message = path_exist(excel_file_path, True)
    if not excel_exists:
        click.echo(f"Error: {message}")
        return
    font_file_exists, message = path_exist(font_file_path, True)
    if not font_file_exists:
        click.echo(f"Error: {message}")
        return
    output_dir_exists, message = path_exist(output_location, False)
    if not output_dir_exists:
        click.echo(f"Error: {message}")
        return
    if not validate_hex(text_color):
        click.echo(f"Error: Text color invalid, please provide Hex color code")
        return
    generate_certificate(
        certificate_image_path,
        excel_file_path,
        text_color,
        x_location,
        y_location,
        bold,
        font_file_path,
        font_size,
        output_location,
    )


if __name__ == "__main__":
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Certi-builder")
    main()