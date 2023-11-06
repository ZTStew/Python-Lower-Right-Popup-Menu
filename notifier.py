from win10toast import ToastNotifier

class notifier:

  def notify(message_title, message_body):
    # Displays Windows notification message for `duration`
    ToastNotifier().show_toast(message_title, message_body, icon_path="./static/clippy - scaled.ico", duration=10)
