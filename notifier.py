from win10toast import ToastNotifier

class notifier:

  def notify(message_title, message_body):
    toaster = ToastNotifier()

    toaster.show_toast(message_title, message_body, icon_path="./static/clippy - scaled.ico", duration=10)
