FROM python:3

ADD login.py /
ADD cross_mark.png /
ADD icon.png /
ADD names_for_numbers.db /
ADD NFN.ico /
ADD student_ui.py /
ADD teacher_ui.py /
ADD tick_mark.py /
RUN pip install numpy
RUN pip install matplotlib
CMD [ "python", "./login.py" ]