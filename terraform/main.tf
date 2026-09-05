# 1. Провайдер AWS і регіон (Stockholm)
provider "aws" {
  region = "eu-north-1"
}

# 2. Мережева безпека (Security Group)
resource "aws_security_group" "calc_sg" {
  name        = "calc-terraform-sg"
  description = "Security group for Calculator App"

  # SSH для підключення через термінал (Порт 22)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Frontend для калькулятора в браузері (Порт 5000)
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Дозвіл серверу завантажувати пакунки з інтернету
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 3. Створення віртуальної машини EC2
resource "aws_instance" "calc_server" {
  #ami = "ami-092cce4a19b438926"
  ami = "ami-0aba19e56f3eaec05"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.calc_sg.id]

  tags = {
    Name = "Calculator-Terraform"
  }
}

# 4. Вивід публічної IP-адреси
output "server_public_ip" {
  value = aws_instance.calc_server.public_ip
}