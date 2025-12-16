import pytest
from unittest.mock import patch, mock_open
from project import load_contacts, save_contacts, add_contact, delete_contact, view_contacts, search_contact

FILE = "contact.csv"

@pytest.fixture
def mock_csv_file():
    mock_data = "name,phone\nFaizs,0179126407\nRizwan,0192888400\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        yield

def test_load_contacts(mock_csv_file):
    """Test loading contacts from a mocked CSV file."""
    contacts = load_contacts()
    assert len(contacts) == 2
    assert contacts[0]['name'] == 'Faizs'
    assert contacts[0]['phone'] == '0179126407'
    assert contacts[1]['name'] == 'Rizwan'
    assert contacts[1]['phone'] == '0192888400'

def test_save_contacts():
    """Test saving contacts to a mocked CSV file."""
    contacts = [{'name': 'Faizs', 'phone': '0179126407'}, {'name': 'Rizwan', 'phone': '0192888400'}]

    with patch("builtins.open", mock_open()) as mock_file:
        save_contacts(contacts)

        # Get the actual calls made to the mock file
        written_calls = [call[0][0] for call in mock_file().write.call_args_list]

        # Verify the expected calls were made
        expected_calls = [
            "name,phone\r\n",
            "Faizs,0179126407\r\n",
            "Rizwan,0192888400\r\n"
        ]
        assert written_calls == expected_calls


def test_add_contact(mock_csv_file):
    """Test adding a contact and verify the output."""
    new_contact_name = "Rizwan"
    new_contact_phone = "0192888400"

    # Add contact
    add_contact(new_contact_name, new_contact_phone)

    # Verify if the contact was added
    contacts = load_contacts()
    assert len(contacts) == 2
    assert contacts[-1]['name'] == new_contact_name
    assert contacts[-1]['phone'] == new_contact_phone

def test_delete_contact(mock_csv_file):
    """Test deleting a contact and verify the output."""
    delete_contact_name = "Rizwan"

    # Delete contact
    delete_contact(delete_contact_name)

    # Verify if the contact was deleted
    contacts = load_contacts()
    assert len(contacts) == 2
    assert contacts[0]['name'] == "Faizs"

def test_view_contacts(mock_csv_file):
    """Test viewing contacts."""
    with patch("builtins.print") as mocked_print:
        view_contacts()

        printed_output = mocked_print.call_args[0][0]

        assert "Faizs" in printed_output
        assert "0179126407" in printed_output
        assert "Rizwan" in printed_output
        assert "0192888400" in printed_output


def test_search_contact(mock_csv_file):
    """Test searching for an existing contact."""
    with patch("builtins.input", side_effect=["0179126407"]), patch("builtins.print") as mocked_print:
        search_contact()

        printed_output = mocked_print.call_args[0][0]

        assert "Faizs" in printed_output
        assert "0179126407" in printed_output
