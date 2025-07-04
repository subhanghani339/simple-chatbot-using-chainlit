import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    response = f"Hello, you just send: {message.content}!"
    await cl.Message(response, "subhan").send()