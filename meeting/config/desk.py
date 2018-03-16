from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Tools"),
            "icon": "oction oction-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("Meeting"),
                    "description": _("Prepare agenta, invite users and record minutes"),
                },
            ]
        }
    ]