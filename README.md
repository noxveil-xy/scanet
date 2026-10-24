# scanet

Инструмент для анализа локальной сети и обнаружения активных устройств.

> Lightweight network reconnaissance and security analysis tool written in Python and Scapy.

![Status](https://img.shields.io/badge/status-BETA-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Analysis-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## About

Проект разрабатывается как практический инструмент для изучения:

- сетевого взаимодействия;
- ARP-протокола;
- обнаружения устройств в локальной сети;
- работы с Ethernet-фреймами;
- анализа IP и MAC-адресов;
- сетевого сканирования;
- Python и Scapy;
- основ сетевой безопасности.

Инструмент предназначен прежде всего для использования в **собственной лабораторной среде и сетях, на которые у пользователя есть разрешение на тестирование**.

---

## Project Status

### Current Version

**BETA — Active Development**

Проект находится в стадии активной разработки.

Текущая реализация является **рабочей beta-версией**, поэтому архитектура, интерфейс и отдельные компоненты могут изменяться.

Некоторые функции находятся на этапе разработки и пока отсутствуют в стабильной реализации.

---

## Current Features

На текущем этапе реализованы следующие возможности.

### Network Discovery

Инструмент выполняет обнаружение активных устройств в указанной IP-подсети.

Используется ARP Request:

```text
ARP Request
     ↓
Broadcast
     ↓
Target Network
     ↓
ARP Response
     ↓
Active Device
