import pandas as pd
import numpy as np
import random
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

file_path = 'Automated_Traffic_Volume_Counts.csv'
data = pd.read_csv(file_path)

data['datetime'] = pd.to_datetime({
    'year': data['Yr'],
    'month': data['M'],
    'day': data['D'],
    'hour': data['HH'],
    'minute': data['MM']
})
data['Volume'] = data['Vol']

simulation_results = []
unique_locations = data.groupby(['Boro', 'street']).size().reset_index()

traffic_volume = data.groupby(['datetime', 'Boro', 'street'])['Volume'].sum().reset_index()
traffic_volume = traffic_volume.sample(frac=1, random_state=42).reset_index(drop=True)
traffic_volume = data.groupby(['Boro', 'street']).head(100).reset_index(drop=True)

class TrafficLightEnv:

    def __init__(self, traffic_data):
        self.traffic_data = traffic_data
        self.current_step = 0
        self.action_space = [0, 1, 2]
        self.state = self.reset()
        
    def reset(self):
        self.current_step = 0
        return {
            'volume': self.traffic_data.iloc[self.current_step]['Volume'],
            'location': (
                self.traffic_data.iloc[self.current_step]['Boro'],
                self.traffic_data.iloc[self.current_step]['street']
            )
        }

    def step(self, action):
        current_volume = self.traffic_data.iloc[self.current_step]['Volume']
        
        if action == 1:
            reward = -current_volume if current_volume > 0 else 0
        elif action == 0:
            reward = current_volume if current_volume > 100 else -50
        else:
            reward = current_volume / 2 if current_volume > 50 else -25

        self.current_step += 1
        if self.current_step >= len(self.traffic_data):
            self.current_step = 0
            done = True
        else:
            done = False

        next_state = {
            'volume': self.traffic_data.iloc[self.current_step]['Volume'],
            'location': (
                self.traffic_data.iloc[self.current_step]['Boro'],
                self.traffic_data.iloc[self.current_step]['street']
            )
        }
        
        return next_state, reward, done

env = TrafficLightEnv(traffic_volume)
state = env.reset()
total_reward = 0
episode_steps = 0
simulation_steps = []

for _ in range(100):
    episode_steps += 1
    volume = state['volume']
    
    if volume > 100:
        action = 1
    elif volume < 50:
        action = 0
    else:
        action = 2
    
    next_state, reward, done = env.step(action)
    total_reward += reward
    
    step_info = {
        'step': episode_steps,
        'location': state['location'],
        'volume': state['volume'],
        'action': 'Verde' if action == 1 else 'Vermelho' if action == 0 else 'Amarelo',
        'reward': reward
    }
    simulation_steps.append(step_info)
    
    state = next_state
    if done:
        break

def create_pdf_report(filename, simulation_steps, total_reward, episode_steps):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    elements.append(Paragraph("Relatório de Simulação de Tráfego", title_style))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph("Resumo da Simulação", styles['Heading2']))
    elements.append(Paragraph(f"Recompensa Total: {total_reward}", styles['Normal']))
    elements.append(Paragraph(f"Total de Passos: {episode_steps}", styles['Normal']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph("Detalhes dos Passos", styles['Heading2']))
    
    table_data = [['Passo', 'Localização', 'Volume', 'Ação', 'Recompensa']]
    
    for step in simulation_steps:
        table_data.append([
            str(step['step']),
            f"{step['location'][0]}, {step['location'][1]}",
            str(step['volume']),
            step['action'],
            str(round(step['reward'], 2))
        ])

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 1),
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),
    ])

    table = Table(table_data)
    table.setStyle(table_style)
    elements.append(table)
    
    doc.build(elements)

create_pdf_report('relatorio_trafego.pdf', simulation_steps, total_reward, episode_steps)
print("Relatório PDF gerado com sucesso: relatorio_trafego.pdf")