from dnslib import DNSRecord, DNSHeader, DNSQuestion, RR, QTYPE, A
from dnslib.server import DNSServer
#pip install dnslib
# Definindo o mapeamento de domínio para IP
DNS_MAP = {
    "linesky.linesky": "192.168.1.5"
}

# Classe customizada de resolução DNS
class DNSResolver:
    def resolve(self, request, handler):
        # Extraindo a questão do DNS
        question = request.q.qname
        domain = str(question).rstrip('.')
        
        # Criando uma resposta DNS
        reply = request.reply()

        # Verificando se o domínio solicitado está no nosso mapeamento
        if domain in DNS_MAP:
            ip_address = DNS_MAP[domain]
            # Adicionando o registro de resposta para o domínio solicitado
            reply.add_answer(RR(question, QTYPE.A, rdata=A(ip_address), ttl=60))
        
        return reply

# Função principal para iniciar o servidor DNS
def start_dns_server():
    resolver = DNSResolver()
    server = DNSServer(resolver, port=53, address="0.0.0.0", tcp=False)
    server.start_thread()
    
    print("Servidor DNS iniciado...")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Servidor DNS encerrado.")
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    start_dns_server()

