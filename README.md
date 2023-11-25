# django-cache
The purpose of this project is learning cacheing in django for large scale project.

## DateTime
in DRF serializer we need to use date field as year-month_number-day_number(2023-12-20),
and time field as 24 hour formate.
By using given settings in django project settings.py file, we can use date and time fields as we need:

```
REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    "DATETIME_INPUT_FORMATS": ["%d-%m-%Y %I:%M %p"],
    "TIME_INPUT_FORMATS": ["%I:%M %p"],
    "TIME_FORMAT": '%I:%M %p',
    "DATE_FORMAT": '%d-%m-%Y',
    "DATETIME_FORMAT": '%d-%m-%Y %I:%M %p'
}
```
