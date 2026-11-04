#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération du rapport technique universitaire en format Word (.docx).
Projet : Analyse de trafic et détection d'anomalies sur les protocoles auxiliaires IPv4 avec Wireshark.
Conforme aux consignes strictes :
- Police Times New Roman intégrale
- Titres de section grands et soulignés, en noir ou gris foncé (pas de couleur vive ni de fond coloré)
- Mise en page sobre et classique, sans fantaisie, marges 2.5 cm, texte justifié
- Pagination soignée (Page X sur Y) dans le pied de page
- Tableaux soignés et sobres (bordures fines, teintes de gris neutres)
- 10 captures d'écran intégrées avec légendes explicatives détaillées
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_report():
    doc = Document()

    # Configuration des marges (2.5 cm partout = env. 0.984 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = False

        # Pied de page avec pagination
        footer = section.footer
        p_foot = footer.paragraphs[0]
        p_foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_foot.paragraph_format.space_before = Pt(0)
        p_foot.paragraph_format.space_after = Pt(0)

        # Texte gauche ou simple numéro à droite
        run_f1 = p_foot.add_run("Rapport technique – Analyse de trafic IPv4 & Wireshark  |  Page ")
        run_f1.font.name = "Times New Roman"
        run_f1.font.size = Pt(9.5)
        run_f1.font.italic = True
        run_f1.font.color.rgb = RGBColor(100, 100, 100)

        # Ajout champ Page
        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')
        instrText1 = OxmlElement('w:instrText')
        instrText1.set(qn('xml:space'), 'preserve')
        instrText1.text = "PAGE"
        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'separate')
        fldChar3 = OxmlElement('w:fldChar')
        fldChar3.set(qn('w:fldCharType'), 'end')
        r_page = p_foot.add_run()._r
        r_page.append(fldChar1)
        r_page.append(instrText1)
        r_page.append(fldChar2)
        r_page.append(fldChar3)

        run_f2 = p_foot.add_run(" / ")
        run_f2.font.name = "Times New Roman"
        run_f2.font.size = Pt(9.5)
        run_f2.font.color.rgb = RGBColor(100, 100, 100)

        # Ajout champ NumPages
        fldChar4 = OxmlElement('w:fldChar')
        fldChar4.set(qn('w:fldCharType'), 'begin')
        instrText2 = OxmlElement('w:instrText')
        instrText2.set(qn('xml:space'), 'preserve')
        instrText2.text = "NUMPAGES"
        fldChar5 = OxmlElement('w:fldChar')
        fldChar5.set(qn('w:fldCharType'), 'separate')
        fldChar6 = OxmlElement('w:fldChar')
        fldChar6.set(qn('w:fldCharType'), 'end')
        r_numpages = p_foot.add_run()._r
        r_numpages.append(fldChar4)
        r_numpages.append(instrText2)
        r_numpages.append(fldChar5)
        r_numpages.append(fldChar6)

    # Configuration des styles par défaut
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(20, 20, 20)

    # Fonctions utilitaires de mise en page
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(18)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.italic = True
        run.font.color.rgb = RGBColor(70, 70, 70)
        return p

    def add_h1(text):
        """Titre de section principal : grand, souligné, sans couleur vive (noir ou gris foncé)."""
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.underline = True
        run.font.color.rgb = RGBColor(20, 20, 20)
        return p

    def add_h2(text):
        """Sous-titre : sobre, gras, taille 12."""
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(40, 40, 40)
        return p

    def add_p(text, bold_prefix=None, space_after=5):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(11)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(20, 20, 20)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(30, 30, 30)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(11)
            r_pre.font.bold = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        return p

    def add_image_with_caption(img_path, caption_text, width_inches=5.8):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(70, 70, 70)

    def style_table(table):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        # Borders XML
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            r'<w:tblBorders %s>'
            r'  <w:top w:val="single" w:sz="6" w:space="0" w:color="A0A0A0"/>'
            r'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="A0A0A0"/>'
            r'  <w:left w:val="none"/>'
            r'  <w:right w:val="none"/>'
            r'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/>'
            r'  <w:insideV w:val="none"/>'
            r'</w:tblBorders>' % nsdecls('w')
        )
        tblPr.append(borders)

    assets_dir = '/tmp/rapport_assets'

    # ==========================================
    # EN-TÊTE / PAGE DE GARDE INTÉGRÉE SOBRE
    # ==========================================
    add_title("RAPPORT TECHNIQUE D'ANALYSE RÉSEAU")
    add_subtitle("Analyse de trafic et détection d'anomalies sur les protocoles auxiliaires IPv4 avec Wireshark\nLaboratoire virtuel VirtualBox (DHCP, ARP, ARP Spoofing, ICMP)")

    # Encadré métadonnées sobre
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(14)
    r_meta = p_meta.add_run("Contexte académique : Laboratoire Réseau & Sécurité IPv4  |  Outil principal : Wireshark / TShark\nEnvironnement de test : Réseau local virtuel isolé (labnet) sous VirtualBox")
    r_meta.font.name = "Times New Roman"
    r_meta.font.size = Pt(10)
    r_meta.font.color.rgb = RGBColor(90, 90, 90)

    # ==========================================
    # SECTION 1 : INTRODUCTION ET ARCHITECTURE DU LAB
    # ==========================================
    add_h1("1. Introduction et architecture du laboratoire")

    add_p(
        "Ce projet a pour objectif d'étudier de manière concrète et approfondie le cycle de vie des protocoles "
        "auxiliaires essentiels de la pile IPv4, d'observer leur comportement nominal et d'identifier les signatures "
        "d'anomalies ou de comportements malveillants sur un réseau local. Les protocoles au cœur de cette étude "
        "comprennent DHCP (attribution et gestion dynamique des configurations IP), ARP (résolution d'adresses entre "
        "couche liaison et couche réseau), et ICMP (contrôle, diagnostic et gestion des contraintes de transmission). "
        "L'énoncé officiel mentionne également IGMP (Internet Group Management Protocol), protocole auxiliaire de gestion "
        "des groupes multicast locaux (adresses 224.0.0.0/4). Bien que les manipulations pratiques du présent laboratoire "
        "se concentrent sur DHCP, ARP et ICMP, le rôle d'IGMP est parfaitement complémentaire pour piloter la diffusion "
        "restreinte aux seuls hôtes abonnés via les routeurs et commutateurs locaux."
    )

    add_h2("1.1. Conception et isolation de l'environnement virtuel")
    add_p(
        "Afin de mener des captures de trafic exhaustives et de simuler des attaques de niveau 2 sans impacter le réseau "
        "physique hôte ni générer de paquets indésirables sur Internet, un environnement virtuel hermétique a été déployé. "
        "Toutes les machines virtuelles sont raccordées à un commutateur virtuel VirtualBox configuré en mode « Réseau interne » "
        "(baptisé labnet). Ce mode garantit un confinement strict du trafic Ethernet et IP au sein des seules machines du TP."
    )

    add_h2("1.2. Plan d'adressage et rôles des machines")
    add_p(
        "Le réseau local retenu est le sous-réseau privé de classe C 192.168.50.0/24 (masque 255.255.255.0). "
        "Trois stations ont été configurées avec des rôles distincts et complémentaires :"
    )

    # Tableau du plan d'adressage
    table_nodes = doc.add_table(rows=4, cols=4)
    style_table(table_nodes)
    headers = ["Machine", "Rôle dans le TP", "Adresse IP", "Adresse MAC"]
    for i, h in enumerate(headers):
        cell = table_nodes.cell(0, i)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EAEAEA"/>')
        cell._tc.get_or_add_tcPr().append(shading)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True

    node_data = [
        ["Mint-Serveur", "Serveur DHCP (isc-dhcp-server), Passerelle du lab", "192.168.50.1 (statique)", "08:00:27:39:ce:5a"],
        ["Mint-Client", "Client DHCP, Station de test & Capture Wireshark", "192.168.50.100 (puis .101)", "08:00:27:c7:b3:6e"],
        ["Kali Linux", "Machine d'audit / Attaquant ARP Spoofing", "192.168.50.102 (statique)", "08:00:27:c3:fb:76"]
    ]

    for row_idx, row in enumerate(node_data, start=1):
        for col_idx, text in enumerate(row):
            cell = table_nodes.cell(row_idx, col_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            if col_idx in [0, 2, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(text)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)

    add_p(
        "La configuration de l'interface réseau principale enp0s3 sur le serveur Linux Mint a été validée à l'aide de "
        "la commande système ip a, illustrée par la capture ci-dessous.",
        space_after=4
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'ip du serveur.png'),
        "Figure 1 : Configuration IP statique de l'interface enp0s3 du serveur (192.168.50.1/24, MAC 08:00:27:39:ce:5a).",
        width_inches=5.8
    )

    # ==========================================
    # SECTION 2 : ÉTAPE DHCP — LE PROCESSUS DORA
    # ==========================================
    add_h1("2. Étape DHCP — Le processus DORA et cycle de vie du bail")

    add_p(
        "Le protocole DHCP (Dynamic Host Configuration Protocol), défini par la RFC 2131, fonctionne au-dessus d'UDP "
        "(ports 67 serveur et 68 client). Il permet à une station cliente sans configuration réseau préalable d'obtenir "
        "dynamiquement l'ensemble des paramètres nécessaires à sa communication : adresse IPv4, masque de sous-réseau, "
        "passerelle par défaut, serveurs DNS et durée de validité de l'attribution (bail DHCP)."
    )

    add_h2("2.1. Analyse séquentielle des quatre messages du cycle DORA")
    add_p(
        "L'initialisation d'un client DHCP non configuré suit une séquence standardisée en quatre temps, désignée sous l'acronyme DORA :"
    )
    add_bullet(
        "DHCP Discover : N'ayant pas encore d'adresse IP valide, le client émet une requête de découverte en diffusion "
        "générale (adresse source 0.0.0.0, adresse destination de diffusion 255.255.255.255). Le message contient l'adresse "
        "MAC physique du client (08:00:27:c7:b3:6e) ainsi qu'un identifiant de transaction aléatoire (Transaction ID, "
        "ici 0x4388ae5f) permettant de corréler les réponses futures.",
        bold_prefix="1. "
    )
    add_bullet(
        "DHCP Offer : Le serveur DHCP (192.168.50.1) réceptionne la découverte, sélectionne une adresse disponible dans "
        "sa plage d'attribution (192.168.50.101) et répond par un message Offer. Cette offre spécifie l'IP proposée (Your IP), "
        "les paramètres réseau (masque /24, passerelle 192.168.50.1), l'identifiant du serveur et la durée du bail.",
        bold_prefix="2. "
    )
    add_bullet(
        "DHCP Request : Le client notifie formellement son acceptation de l'offre reçue en émettant un message Request. "
        "Cette trame est à nouveau transmise en diffusion (Broadcast) afin d'avertir simultanément l'ensemble des éventuels "
        "serveurs DHCP du sous-réseau que cette offre précise a été retenue, libérant les propositions concurrentes.",
        bold_prefix="3. "
    )
    add_bullet(
        "DHCP Acknowledge (ACK) : Le serveur valide définitivement l'attribution en envoyant un accusé de réception (ACK). "
        "L'adresse 192.168.50.101 est alors enregistrée dans la table des baux actifs du serveur, et le client configure son interface.",
        bold_prefix="4. "
    )

    add_h2("2.2. Commandes d'administration et forçage de renouvellement")
    add_p(
        "Pour tester et observer ce processus sous Wireshark, les outils clients Linux ISC-DHCP ont été exécutés sur Mint-Client :"
    )
    add_bullet(
        "sudo dhclient -r enp0s3 : Cette commande libère le bail courant en émettant un paquet DHCP Release à destination "
        "du serveur (visible à la trame n°57 sur la capture Wireshark, transaction 0x92466642). Le serveur remet alors l'adresse "
        "dans le pool d'adresses disponibles.",
        bold_prefix="• Libération du bail courant : "
    )
    add_bullet(
        "sudo dhclient -v enp0s3 : Lance une nouvelle négociation DHCP en mode verbeux, forçant l'émission d'un Discover "
        "sur l'interface réseau enp0s3.",
        bold_prefix="• Négociation d'un nouveau bail : "
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'commande_renouv_bail.png'),
        "Figure 2 : Commandes d'administration dhclient exécutées sur le client (libération et nouvelle négociation).",
        width_inches=4.8
    )

    add_h2("2.3. Durée de bail raccourcie et mécanisme de renouvellement à mi-bail (T1)")
    add_p(
        "Dans la configuration du serveur (/etc/dhcp/dhcpd.conf), la durée de validité du bail a été volontairement fixée "
        "à une valeur courte de 600 secondes (10 minutes). Conformément à la norme RFC 2131, deux compteurs régissent la vie du bail :"
    )
    add_bullet(
        "Le temps T1 (renouvellement) fixé à 50% de la durée totale, soit environ 300 secondes. Dès que ce délai est atteint, "
        "le client tente de prolonger son bail directement auprès du serveur initial.",
        bold_prefix="• Minuteur T1 (50%) : "
    )
    add_bullet(
        "Le temps T2 (rebinding) fixé à 87.5% de la durée (environ 525 secondes), déclenché uniquement si le serveur initial ne répond pas.",
        bold_prefix="• Minuteur T2 (87.5%) : "
    )
    add_p(
        "L'observation attentive de la capture Wireshark confirme rigoureusement ce mécanisme :"
    )
    add_bullet(
        "Cycle initial DORA complet aux trames 60 à 64 (temps relatif t ≈ 50s à 51.8s) : Discover (t=50.39s), Offer (t=51.40s), "
        "Request (t=51.40s) et ACK (t=51.81s) avec la Transaction ID 0x4388ae5f, attribuant l'IP 192.168.50.101.",
        bold_prefix="• Attribution initiale : "
    )
    add_bullet(
        "Renouvellement automatique aux trames 367 et 368 (temps relatif t ≈ 319.23s, soit exactement 268 secondes après l'ACK initial, "
        "très proche du seuil théorique T1 de 300 secondes). Le client émet un DHCP Request directement en Unicast depuis "
        "192.168.50.101 vers 192.168.50.1. Le serveur répond immédiatement par un DHCP ACK unicast (trame 368). "
        "Ce renouvellement n'a nécessité ni Discover ni Offer, optimisant la charge réseau.",
        bold_prefix="• Renouvellement à T1 : "
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'DORA+renouveau bail.png'),
        "Figure 3 : Capture Wireshark du trafic DHCP montrant le cycle DORA initial (trames 60-64) et le renouvellement de bail unicast à T1 (trames 367-368).",
        width_inches=6.0
    )

    # ==========================================
    # SECTION 3 : ÉTAPE ARP — RÉSOLUTION D'ADRESSES
    # ==========================================
    add_h1("3. Étape ARP — Résolution d'adresses et inspection des trames")

    add_p(
        "Le protocole ARP (Address Resolution Protocol), standardisé par la RFC 826, opère directement sur la couche liaison "
        "(couche 2 du modèle OSI, EtherType 0x0806). Sa fonction fondamentale est de faire correspondre une adresse logique de "
        "couche 3 (adresse IPv4) à une adresse matérielle physique de couche 2 (adresse MAC), indispensable pour l'encapsulation "
        "et la livraison des trames Ethernet sur le segment local."
    )

    add_h2("3.1. Manipulation de la table ARP et déclenchement de la résolution")
    add_p(
        "Pour contraindre le système d'exploitation à exécuter une résolution ARP complète, la séquence suivante a été réalisée sur Mint-Client :"
    )
    add_bullet(
        "Consultation de la table de correspondance existante à l'aide de arp -a, affichant l'association nominale entre la passerelle "
        "192.168.50.1 et son adresse MAC 08:00:27:39:ce:5a.",
        bold_prefix="1. État initial : "
    )
    add_bullet(
        "Purge de l'entrée du cache à l'aide de la commande sudo arp -d 192.168.50.1.",
        bold_prefix="2. Suppression de l'entrée : "
    )
    add_bullet(
        "Émission de paquets ICMP vers 192.168.50.1 (ping -c 3 192.168.50.1). Le noyau ne possédant plus l'adresse MAC de destination "
        "pour encapsuler le paquet IP, met l'émission ICMP en attente et déclenche immédiatement une requête ARP.",
        bold_prefix="3. Requête déclenchée par un ping : "
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'arp commande.png'),
        "Figure 4 : Commandes de gestion du cache ARP (arp -a, arp -d) et exécution du ping déclencheur sur le client.",
        width_inches=4.8
    )

    add_h2("3.2. Analyse détaillée du trafic ARP dans Wireshark")
    add_p(
        "En appliquant le filtre d'affichage arp dans Wireshark, les deux phases de la résolution sont nettement observables :"
    )
    add_bullet(
        "ARP Request (trame 48, t=46.49s) : Le client Mint diffuse une requête en broadcast Ethernet (adresse MAC destination "
        "ff:ff:ff:ff:ff:ff). L'information textuelle indique : « Who has 192.168.50.1? Tell 192.168.50.100 ». Toutes les machines "
        "du réseau interne reçoivent la trame, mais seule celle possédant l'IP demandée traite la demande.",
        bold_prefix="• Requête en diffusion (Broadcast) : "
    )
    add_bullet(
        "ARP Reply (trame 49, t=46.49s) : Le serveur Mint-Serveur répond immédiatement en Unicast direct à l'adresse MAC du client "
        "(08:00:27:c7:b3:6e). Le contenu de la réponse est explicite : « 192.168.50.1 is at 08:00:27:39:ce:5a ». À réception, le client "
        "met à jour son cache dynamique et libère l'envoi des paquets ICMP Echo Request.",
        bold_prefix="• Réponse en point-à-point (Unicast) : "
    )
    add_bullet(
        "Trames 86-87 (t=81.69s) et 97-98 (t=95.63s) : On observe des échanges similaires de maintien ou de vérification périodique "
        "entre les deux hôtes légitimes.",
        bold_prefix="• Rafraîchissements ultérieurs : "
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'arp.png'),
        "Figure 5 : Capture Wireshark montrant la séquence ARP Request (Broadcast, trame 48) et ARP Reply (Unicast, trame 49).",
        width_inches=6.0
    )

    # ==========================================
    # SECTION 4 : ÉTAPE ARP SPOOFING — DÉTECTION D'UNE USURPATION
    # ==========================================
    add_h1("4. Étape ARP Spoofing — Simulation, analyse statistique et détection")

    add_p(
        "Le protocole ARP a été conçu à l'origine dans un environnement de confiance mutuelle, sans aucun mécanisme d'authentification "
        "ni de signature cryptographique. Cette absence de vérification le rend structurellement vulnérable à l'attaque dite "
        "d'usurpation ARP (ARP Spoofing ou ARP Poisoning)."
    )

    add_h2("4.1. Principe de l'attaque de l'homme du milieu (Man-in-the-Middle)")
    add_p(
        "L'attaque a été simulée depuis la machine virtuelle Kali Linux (192.168.50.102, MAC 08:00:27:c3:fb:76) à l'aide de l'outil "
        "arpspoof. Le principe consiste à injecter en flux continu des réponses ARP falsifiées et non sollicitées (Gratuitous ARP / "
        "Unsolicited Replies) :"
    )
    add_bullet(
        "À destination du client Mint (192.168.50.100), l'attaquant affirme : « L'adresse IP 192.168.50.1 est associée à l'adresse "
        "MAC 08:00:27:c3:fb:76 (adresse MAC de Kali) ».",
        bold_prefix="• Empoisonnement du client : "
    )
    add_bullet(
        "À destination du serveur Mint (192.168.50.1), l'attaquant affirme symétriquement : « L'adresse IP 192.168.50.100 est "
        "associée à l'adresse MAC 08:00:27:c3:fb:76 ».",
        bold_prefix="• Empoisonnement du serveur : "
    )
    add_p(
        "Les caches ARP des deux machines cibles sont alors corrompus. En activant le routage IP sur Kali (sysctl -w net.ipv4.ip_forward=1), "
        "la totalité du trafic échangé entre le client et le serveur transite désormais de façon transparente par Kali Linux, qui "
        "devient un intermédiaire discret capable d'intercepter, modifier ou rejouer les communications."
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'verif_de attaque_reussi sur le client.png'),
        "Figure 6 : Constat de la présence de la machine attaquante Kali (MAC 08:00:27:c3:fb:76) dans la table du client.",
        width_inches=4.5
    )

    add_h2("4.2. Détection avancée par les statistiques Wireshark (Conversations & Endpoints)")
    add_p(
        "La détection formelle de l'attaque s'appuie sur le module Statistiques → Conversations de Wireshark. Deux observations majeures "
        "confirment incontestablement le détournement :"
    )
    add_bullet(
        "Onglet Ethernet : La fenêtre Conversations liste les flux au niveau de la couche liaison 2. On y observe une asymétrie flagrante : "
        "la conversation entre le client (08:00:27:c7:b3:6e) et Kali (08:00:27:c3:fb:76) totalise un volume massif de 373 paquets "
        "(représentant 22 ko de données), alors que la conversation directe entre le client et le serveur légitime (08:00:27:39:ce:5a) "
        "ne compte que 2 paquets (102 octets). Le flux direct est quasiment éteint, prouvant que tout le trafic est capté par Kali.",
        bold_prefix="1. Analyse des volumes Ethernet : "
    )
    add_bullet(
        "Onglet IPv4 vide sous filtre ARP : Lorsque l'administrateur active l'option « Limiter au filtre d'affichage » avec un filtre ARP, "
        "l'onglet IPv4 de la boîte de dialogue Conversations apparaît totalement vide. Ce comportement est tout à fait normal et logique : "
        "ARP est un protocole de niveau 2 (directement encapsulé dans la trame Ethernet avec EtherType 0x0806). Ne contenant aucun "
        "en-tête IP de niveau 3, Wireshark ne recense aucune conversation IPv4 pour ces trames.",
        bold_prefix="2. Onglet IPv4 vide et justification protocolaire : "
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'conversations_ethernet.png'),
        "Figure 7 : Statistiques des conversations Ethernet sous Wireshark montrant le détournement de trafic vers Kali (373 paquets vers 08:00:27:c3:fb:76 contre 2 paquets vers le serveur légitime).",
        width_inches=5.8
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'conversations_ipv4.png'),
        "Figure 8 : Onglet IPv4 des conversations Wireshark vide sous filtre ARP (justifié par l'absence d'en-tête de couche 3).",
        width_inches=5.6
    )

    add_h2("4.3. Rétablissement du cache et remédiation")
    add_p(
        "Une fois l'outil arpspoof arrêté, la table ARP du client a été purgée à nouveau par sudo arp -d 192.168.50.1, puis un test de "
        "connectivité (ping -c 2 192.168.50.1) a régénéré une entrée saine. L'affichage arp -a confirme la restauration de la véritable "
        "adresse MAC du serveur légitime (08:00:27:39:ce:5a)."
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'apres_attaque.png'),
        "Figure 9 : Rétablissement de la table ARP du client après fin de l'attaque et validation de l'adresse MAC nominale du serveur.",
        width_inches=4.8
    )

    # ==========================================
    # SECTION 5 : ÉTAPE ICMP — DIAGNOSTICS ET FRAGMENTATION
    # ==========================================
    add_h1("5. Étape ICMP — Diagnostics réseau et fragmentation IP")

    add_p(
        "Le protocole ICMP (Internet Control Message Protocol), défini par la RFC 792, est le protocole de diagnostic et de gestion "
        "d'erreurs de la couche réseau IPv4 (protocole IP n°1). Il est couramment utilisé par l'utilitaire ping (Echo Request type 8, "
        "Echo Reply type 0) et par traceroute (messages Time Exceeded type 11 code 0 lorsque le TTL expire)."
    )

    add_h2("5.1. Test de connectivité standard (sans fragmentation)")
    add_p(
        "Lors d'un ping classique sous Linux (sans argument particulier de taille), la charge utile ICMP est de 56 octets de données "
        "auxquels s'ajoutent 8 octets d'en-tête ICMP (soit 64 octets ICMP au total). Avec l'en-tête IPv4 (20 octets) et l'en-tête Ethernet "
        "(14 octets), la taille totale sur le support physique est exactement de 98 octets. Ce format standard est visible aux trames "
        "53 à 64 de la capture Wireshark (Longueur : 98, Echo Request / Echo Reply réguliers)."
    )

    add_h2("5.2. Test de surcharge et mécanisme de fragmentation IP")
    add_p(
        "Afin d'étudier le comportement d'IPv4 face à des données volumineuses, un second test a été réalisé en modifiant la taille "
        "des données transportées grâce à l'option -s de la commande ping :"
    )
    p_cmd = doc.add_paragraph()
    p_cmd.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c = p_cmd.add_run("ping -s 2000 192.168.50.1")
    r_c.font.name = "Times New Roman"
    r_c.font.size = Pt(11)
    r_c.font.bold = True

    add_p(
        "Le MTU (Maximum Transmission Unit) standard d'une interface réseau Ethernet (enp0s3) est configuré à 1500 octets. "
        "Le MTU représente la taille maximale admissible pour un paquet IP complet (en-tête IP + données de niveau supérieur) "
        "sur une trame Ethernet sans provoquer de fragmentation."
    )

    add_h2("5.3. Justification mathématique et calcul détaillé des fragments")
    add_p(
        "Voici la décomposition rigoureuse des paquets observés dans la capture Wireshark :"
    )
    add_bullet(
        "Charge totale générée par la couche ICMP : 2000 octets (charge utile spécifiée par -s 2000) + 8 octets (en-tête ICMP comprenant "
        "le type, le code, le checksum, l'identifiant et le numéro de séquence) = 2008 octets.",
        bold_prefix="• Charge ICMP totale : "
    )
    add_bullet(
        "Capacité maximale de données par fragment IP : MTU (1500 octets) − En-tête IPv4 standard (20 octets) = 1480 octets. "
        "Le protocole IP impose que le champ Fragment Offset soit un multiple de 8 octets, ce qui est parfaitement respecté "
        "(1480 / 8 = 185 blocs de 8 octets).",
        bold_prefix="• Premier fragment IP : "
    )
    add_bullet(
        "Taille du premier fragment sur le câble : 1480 octets de données + 20 octets d'en-tête IP + 14 octets d'en-tête Ethernet = 1514 octets "
        "(le drapeau More Fragments MF est positionné à 1, Offset = 0).",
        bold_prefix="• Taille filaire du fragment 1 : "
    )
    add_bullet(
        "Données restantes à transporter : 2008 octets − 1480 octets = 528 octets de données ICMP résiduelles.",
        bold_prefix="• Données résiduelles : "
    )
    add_bullet(
        "Taille du second fragment sur le câble : 528 octets de données + 20 octets d'en-tête IP + 14 octets d'en-tête Ethernet = 562 octets. "
        "Le drapeau More Fragments est à 0 (dernier fragment) et l'Offset vaut 1480 octets (soit 185 blocs).",
        bold_prefix="• Taille filaire du fragment 2 : "
    )
    add_p(
        "Ce calcul mathématique démontre avec une précision absolue pourquoi la trame n°210 affichée dans Wireshark présente très exactement "
        "la mention « Frame 210: 562 bytes on wire (4496 bits), 562 bytes captured » ainsi que la mention "
        "« [Reassembled IPv4 (2008 bytes)] ». Wireshark a intercepté les 528 octets restants et reconstitué avec succès l'intégralité du "
        "paquet ICMP de 2008 octets transmis par la pile réseau."
    )

    add_image_with_caption(
        os.path.join(assets_dir, 'modif de la taille des paquets.png'),
        "Figure 10 : Capture Wireshark du trafic ICMP avec modification de taille (-s 2000). Détail du fragment n°210 (562 octets sur le fil) et confirmation du réassemblage IPv4 de 2008 octets.",
        width_inches=6.0
    )

    # ==========================================
    # SECTION 6 : CONCLUSION GÉNÉRALE
    # ==========================================
    add_h1("6. Conclusion générale")

    add_p(
        "Ce projet en environnement virtuel isolé a permis de confronter les concepts théoriques de la pile TCP/IPv4 à leur "
        "comportement dynamique réel sur le fil. Les trois protocoles auxiliaires examinés ont révélé leurs rôles indispensables "
        "ainsi que leurs faiblesses inhérentes :"
    )
    add_bullet(
        "Le protocole DHCP assure l'automatisation intégrale de l'adressage au travers d'un dialogue DORA rigoureux et maintient "
        "l'intégrité des allocations par des renouvellements unicast efficaces déclenchés à mi-bail (T1).",
        bold_prefix="• Automatisation et cycle de vie : "
    )
    add_bullet(
        "Le protocole ARP remplit un rôle pivot pour assurer la transition entre le monde logique (IP) et physique (Ethernet), "
        "mais son absence native de sécurité et d'authentification expose les réseaux locaux aux attaques redoutables d'usurpation "
        "(ARP Spoofing / Man-in-the-Middle).",
        bold_prefix="• Vulnérabilité structurelle de niveau 2 : "
    )
    add_bullet(
        "Le protocole ICMP s'avère un instrument de diagnostic incontournable pour jauger la connectivité et a mis en exergue les "
        "mécanismes de découpage et de réassemblage de la fragmentation IP régis par le MTU de l'interface physique.",
        bold_prefix="• Diagnostic et gestion des limites physiques : "
    )
    add_bullet(
        "Wireshark s'est affirmé comme un outil d'inspection et de supervision irremplaçable, non seulement par son analyseur de "
        "paquets protocolaire, mais surtout par ses outils de statistiques croisées (Conversations Ethernet) capables de révéler "
        "des détournements de flux invisibles au niveau applicatif.",
        bold_prefix="• Rôle déterminant de l'analyseur : "
    )

    # ==========================================
    # SECTION 7 : NOTE DE SYNTHÈSE SUR LES FILTRES WIRESHARK
    # ==========================================
    add_h1("7. Note de synthèse : Maîtrise des filtres avancés de Wireshark pour la détection d'anomalies et de congestions")

    add_p(
        "Conformément au second livrable attendu, cette note de synthèse formalise les bonnes pratiques et les filtres d'affichage "
        "avancés indispensables à un administrateur système ou analyste de sécurité pour diagnostiquer rapidement des congestions, "
        "isoler des pannes ou détecter des activités malveillantes sur un réseau local IPv4."
    )

    add_h2("7.1. Synthèse des filtres protocolaires fondamentaux utilisés")

    # Tableau des filtres clés
    table_filters = doc.add_table(rows=6, cols=3)
    style_table(table_filters)
    f_headers = ["Protocole / Objectif", "Filtre d'affichage Wireshark", "Description et utilité opérationnelle"]
    for i, h in enumerate(f_headers):
        cell = table_filters.cell(0, i)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EAEAEA"/>')
        cell._tc.get_or_add_tcPr().append(shading)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True

    filters_data = [
        ["DHCP global", "dhcp ou bootp", "Isole l'ensemble des échanges d'attribution et de renouvellement dynamique (DORA, Release, Inform)."],
        ["Résolution ARP", "arp", "Affiche toutes les requêtes en diffusion (who-has) et les réponses unicast (is-at)."],
        ["Détection d'usurpation ARP", "arp.duplicate-address-detected", "Alerte de sécurité majeure émise par le moteur d'analyse de Wireshark lorsqu'une même adresse IP est revendiquée par deux adresses MAC distinctes (signature directe d'ARP Spoofing)."],
        ["Requêtes ARP non sollicitées", "arp.opcode == 2 and eth.dst == ff:ff:ff:ff:ff:ff", "Détecte les Gratuitous ARP émis en broadcast, fréquemment exploités pour empoisonner massivement les tables ARP d'un réseau."],
        ["Diagnostics ICMP & Fragmentation", "icmp or ip.flags.mf == 1 or ip.frag_offset > 0", "Isole les paquets de diagnostic (ping, traceroute) ainsi que tous les fragments IP circulant sur le réseau."]
    ]

    for row_idx, row in enumerate(filters_data, start=1):
        for col_idx, text in enumerate(row):
            cell = table_filters.cell(row_idx, col_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(text)
                r.font.bold = True
            elif col_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(text)
                r.font.name = "Courier New"
                r.font.size = Pt(9)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                r = p.add_run(text)
            r.font.name = "Times New Roman" if col_idx != 1 else "Courier New"
            r.font.size = Pt(9.5) if col_idx != 1 else Pt(9)

    add_h2("7.2. Filtres avancés pour la détection d'anomalies de sécurité")
    add_bullet(
        "bootp.type == 1 and not (ip.src == 0.0.0.0) : Détecte des requêtes DHCP suspectes provenant d'hôtes possédant déjà une adresse "
        "IP active, pouvant signaler une tentative d'épuisement de pool DHCP (DHCP Starvation).",
        bold_prefix="• Détection de requêtes DHCP illégitimes : "
    )
    add_bullet(
        "bootp.type == 2 and not (ip.src == 192.168.50.1) : Repère l'apparition d'un serveur DHCP pirate (Rogue DHCP Server) offrant des "
        "baux non autorisés afin de détourner la passerelle par défaut.",
        bold_prefix="• Détection de serveurs DHCP pirates : "
    )
    add_bullet(
        "icmp.type == 3 and (icmp.code == 1 or icmp.code == 3) : Isole les réponses d'inaccessibilité (Host Unreachable ou Port Unreachable), "
        "indicateurs fréquents d'un balayage de ports ou d'une cartographie réseau active.",
        bold_prefix="• Détection de scans réseau par ICMP : "
    )

    add_h2("7.3. Filtres avancés pour l'analyse des congestions et goulets d'étranglement")
    add_bullet(
        "tcp.analysis.retransmission : Filtre capital pour isoler les paquets réémis en raison de pertes sur le lien ou de tampons saturés.",
        bold_prefix="• Retransmissions TCP : "
    )
    add_bullet(
        "tcp.analysis.zero_window : Alerte lorsqu'un récepteur informe l'émetteur que sa mémoire tampon de réception est comblée, gelant la transmission.",
        bold_prefix="• Saturation de fenêtre (ZeroWindow) : "
    )
    add_bullet(
        "eth.dst[0] & 1 : Isole l'ensemble des trames de diffusion (Broadcast) et de multidiffusion (Multicast). Un taux anormalement "
        "élevé (> 10-15% du trafic global) signale une tempête de broadcast (Broadcast Storm) susceptible d'effondrer les commutateurs locaux.",
        bold_prefix="• Surveillance des tempêtes de broadcast : "
    )

    output_path = "/app/rapport technique.docx"
    doc.save(output_path)
    print(f"Rapport technique Word généré avec succès : {output_path}")

if __name__ == "__main__":
    create_report()
