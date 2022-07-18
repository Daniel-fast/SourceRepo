from twilio.rest import Client

account_SID = "ACd2387e5fea957a4d845476a74518432d"

auth_token = "03bdda388cc5481a10273e803451b301"

message = "Acorda Thammy"


client = Client(account_SID, auth_token)

call = client.messages.create(
    to="+5511994954119",
    from_="+15087197228",
    body="Olha que eu fiz Thammy!!!"
)

data_envio = call.date_sent

print("Mensagem enviada em: ", data_envio)
