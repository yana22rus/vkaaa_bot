from os import getenv, listdir
from random import randrange
from vk_api import VkApi, VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from models import add_id_user

vk_session = VkApi(token=getenv('token'))

api_session = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def random_files(path,extension):
    files = listdir(path)

    return f"{path}{randrange(1, len(files))}.{extension}"


upload = VkUpload(vk_session)


def send_random_photo(id_user):
    vk_session.method("messages.send",
                      {"user_id": id_user, "random_id": get_random_id(), "attachment": ",".join(attachments)})

def send_random_gif(id_user):
    vk_session.method("messages.send",
                      {"user_id": id_user, "random_id": get_random_id(), "attachment": ",".join(attachments)})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()

            id_user = event.user_id

            if msg.lower() in ["2","фото","photo","/фото","/photo","фотку","фотки"]:
                attachments = []

                upload_image = upload.photo_messages(photos=random_files(getenv("path_to_photo"),"jpg"))[0]

                attachments.append(f"photo{upload_image['owner_id']}_{upload_image['id']}")

                send_random_photo(id_user)

                add_id_user(id_user)

            if msg.lower() in ["1","гиф","gif","/гиф","/gif","гифку","гифки"]:
                attachments = []

                upload_gif = upload.document_message(doc=random_files(getenv("path_to_gif"),"gif"), peer_id=id_user)

                attachments.append(f"doc{upload_gif['doc']['owner_id']}_{upload_gif['doc']['id']}")

                send_random_gif(id_user)

                add_id_user(id_user)

