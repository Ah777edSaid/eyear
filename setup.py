# setup.py

from setuptools import setup

setup(
    name="my_python_project",  # اسم المشروع
    version="0.1",  # رقم الإصدار
    py_modules=["my_script"],  # اسم الملف .py بدون الامتداد
    install_requires=[],  # إذا كان لديك مكتبات أخرى يجب تثبيتها مع المشروع
    entry_points={
        "console_scripts": [
            "my-python-project=my_script:hello_world",  # أمر لتشغيل الكود من الطرفية
        ],
    },
)
