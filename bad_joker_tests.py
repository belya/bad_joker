import unittest
from bad_joker import bad_joker, _generate_joke, _generate_default_joke
from unittest.mock import patch, MagicMock
import os

class BadJokerTestCase(unittest.TestCase):
  def test_generate_joke(self):
    joke = _generate_joke("Something")
    assert "Something" in joke

  def test_generate_default_joke(self):
    joke = _generate_default_joke()
    assert joke

  def test_send_message_with_process_output(self):
    test_messages_mock = MagicMock()
    test_joke_mock =  MagicMock(return_value="test joke")
    with patch('telegram_send.send', test_messages_mock), \
         patch('bad_joker._generate_default_joke', test_joke_mock):
      bad_joker("echo test")
      test_joke_mock.assert_called_with()
      test_messages_mock.assert_called_with(["test joke"])

  def test_send_joke_if_exception(self):
    test_messages_mock = MagicMock()
    test_joke_mock = MagicMock(return_value="joke")
    with open("/tmp/test_exception.py", "w") as f:
      f.write("raise Exception('I am down')")
    with patch('telegram_send.send', test_messages_mock), \
         patch("bad_joker._generate_joke", test_joke_mock):
      bad_joker("python3 /tmp/test_exception.py")
      assert "Traceback" in test_joke_mock.call_args[0][0]
      test_messages_mock.assert_called_with(["joke"])
    os.remove("/tmp/test_exception.py")