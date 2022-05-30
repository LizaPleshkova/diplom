from django.core.management.base import BaseCommand, CommandError

import pdfkit
# from wkhtmltopdf import WKHtmlToPdf


class Command(BaseCommand):

    def handle(self, *args, **options):
        config = pdfkit.configuration(
            wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        # pdfkit.from_url("http://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/",
                        # "out.pdf", configuration=config)
        pdfkit.from_url('http://google.com', 'out.pdf', configuration=config)

        # wkhtmltopdf = WKHtmlToPdf(
        #     url='http://google.com',
        #     output_file='out.pdf',
        # )
        # wkhtmltopdf.render()

        # print("user = ", user)
        # UserService.download_tickets()
        # # with open(f'static/tickets/out.pdf') as f:
        # #     print('heeeeeeere', f)
        #
        # short_report = open("static/tickets/out.pdf", 'rb')
        # response = HttpResponse(FileWrapper(short_report), content_type='application/pdf', status=status.HTTP_200_OK)
        # return response