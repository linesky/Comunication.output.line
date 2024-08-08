
from dnslib import DNSRecord, QTYPE
import socket
#pip install dnslib
def dns_request(domain, dns_server):
    # Criando o pacote DNS com a consulta para o domínio fornecido
    q = DNSRecord.question(domain)
    
    # Convertendo o pacote DNS para bytes
    q_data = q.pack()
    
    # Criando um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enviando o pacote DNS para o servidor DNS especificado
    sock.sendto(q_data, (dns_server, 53))
    
    # Recebendo a resposta do servidor DNS
    response_data, _ = sock.recvfrom(1024)
    
    # Fechando o socket
    sock.close()
    
    # Decodificando a resposta do servidor
    response = DNSRecord.parse(response_data)
    
    return response
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    domain = "skyline.skyline"
    domain = input("domanin:")
    
    dns_server = "192.168.1.5"
    
    # Fazendo a requisição DNS
    response = dns_request(domain, dns_server)
    
    # Imprimindo a resposta recebida
    print("Resposta DNS para o domínio:", domain)
    print(response)
