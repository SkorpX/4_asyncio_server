import asyncio

async def handle_echo(host, port):
	addr = port.get_extra_info('peername')

	while True:
		data = await host.read(100)
		message = data.decode()

		if message == 'exit':
			port.close()
			print (addr, 'disconnect')
			break
		msg = str(addr) + ' write the message - ' + message
		port.write(msg.encode())
		await port.drain()
		print (msg)

loop = asyncio.get_event_loop()
task = asyncio.start_server(handle_echo, '', 9090, loop=loop)
server = loop.run_until_complete(task)
try:
	loop.run_forever()
except KeyboardInterrupt:
	pass