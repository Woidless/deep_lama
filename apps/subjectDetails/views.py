from django.views.generic import ListView
from django.db import connection

from .forms import SubjectDetailsForm

class SubjectDetailsListView(ListView):
    template_name = 'subjectdetails/subject_details_list.html'
    context_object_name = 'subject_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SubjectDetailsForm()  # Assuming you have a form for something else
        context['form'] = form
        # Fetch data from the SubjectDetails view using raw SQL query
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM SubjectDetails")
            rows = cursor.fetchall()
            subject_details = []
            for row in rows:
                subject_detail = {
                    'study_cycle': row[0],
                    'subject': row[1],
                    'education_form': row[2],
                    'number_of_students': row[3],
                    'textbooks': row[4].split(', ') if row[4] else [],  # Split textbooks string into a list
                    'web_materials': row[5].split(', ') if row[5] else [],  # Split web_materials string into a list
                }
                subject_details.append(subject_detail)
            context['subject_details'] = subject_details
        return context

    def get_queryset(self):
        # Return an empty queryset
        return []