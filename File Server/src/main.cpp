#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <thread>

#include <arpa/inet.h>
#include <sys/socket.h>

namespace fs = std::filesystem;

void handleConnection(int c_sock) {
	char buf[4098];
	recv(c_sock, buf, 4098, 0);
	std::string method, uri, version, content;
	std::stringstream(buf) >> method >> uri >> version;
	if (method != "GET") return; // Line count too little to return a 502 response
	uri = '.' + uri;
	if (uri == "./") {
		std::cout << "Serving directory " << uri << std::endl;
		content =
			"<!DOCTYPE html>\n"
			"<head>\n"
			"\t<title>HTTP File Server</title>\n"
			"</head>\n"
			"<body>\n"
			"<h1>You are in '<code>" + uri + "</code>'</h1>\n"
			"\t<ul>\n";
		for (auto& file : fs::directory_iterator(uri)) {
			if (!file.is_directory()) content += "\t\t<li><a href=" + static_cast<std::string>(file.path().c_str()) + ">" + static_cast<std::string>(file.path().c_str()) + "</a></li>\n";
		}
		content += "\t</ul>"
			"\n</body>\n"
			"\r\n\r\n";
	} else {
		std::ifstream file(uri);
		std::cout << "Serving file " << uri << std::endl;
		std::string temp;
		while (std::getline(file, temp)) {
			content += temp + "\n";
		}
		file.close();
	}
	std::stringstream response;
	response << "HTTP/1.1 200 OK\r\n"
		<< "server: SimpleFileServer/0.0.0\r\n"
		<< "content-length: " << content.size() << "\r\n"
		<< "\r\n"
		<< content;
	send(c_sock, response.str().c_str(), response.str().size(), 0);
}

int main() {
	const int port = 3000;
	auto s_sock = socket(AF_INET, SOCK_STREAM, 0);
	{
		int val = 1;
		setsockopt(s_sock, SOL_SOCKET, SO_REUSEADDR, &val, sizeof(val));
	}
	sockaddr_in s_info;
	s_info.sin_family = AF_INET;
	s_info.sin_addr.s_addr = INADDR_ANY;
	s_info.sin_port = htons(port);

	if (bind(s_sock, reinterpret_cast<sockaddr*>(&s_info), sizeof(s_info)) < 0) return -1;
	if (listen(s_sock, 5) < 0) return -2;

	std::cout << "Server is running on 0.0.0.0:" << port << "\n\tClose with ^C" << std::endl;
	while (true) {
		int c_sock;
		sockaddr_in c_info;
		socklen_t c_size = sizeof(c_info);
		if ((c_sock = accept(s_sock, reinterpret_cast<sockaddr*>(&c_info), &c_size)) < 0) continue;
		std::thread c_thread(handleConnection, c_sock);
		c_thread.detach();
	}
}
