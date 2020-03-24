from scheduling.models import Schedule


def get_all_data():
    all_data = Schedule.objects.all()
    return all_data
