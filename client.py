import asyncio

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('localhost', 9090)

    while True:
    	message = input('> ')
    	writer.write(message.encode())
    	if message == 'exit':
    		writer.close()
    		print('Goodbye!')
    		break
    	data = await reader.read(100)

loop = asyncio.get_event_loop()
task = loop.create_task(tcp_echo_client())
loop.run_until_complete(task)
