from ._anvil_designer import ItemTemplate43Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import main_form_module as main_form_module

class ItemTemplate43(ItemTemplate43Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.user_id = main_form_module.userId   
    user_data = app_tables.fin_loan_details.search(loan_updated_status=q.like('reject%'), borrower_customer_id=self.user_id)
    for row in user_data:
        borrower_customer_id = row['borrower_customer_id']
        lender_customer_id = row['lender_customer_id']
        borrower_profile = app_tables.fin_user_profile.get(customer_id=borrower_customer_id)
        lender_profile = app_tables.fin_user_profile.get(customer_id=lender_customer_id)
        self.image_1.source = lender_profile['user_photo']
        self.mobile.text = lender_profile['mobile']


    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    selcted_row=self.item
    open_form('borrower_registration_form.dashboard.view_loans.view_profile',selected_row=selcted_row)
