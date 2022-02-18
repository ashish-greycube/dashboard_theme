import frappe

def update_website_context(context):
	context["website_context"] = {
    "splash_image": "/assets/dashboard_theme/images/dash-logo.svg"
}