CATEGORIES = [
    {"id": "gouvernance",   "label": "Gouvernance & Organisation",   "icon": "🏛️", "weight": 1.0},
    {"id": "registre",      "label": "Registre des traitements",     "icon": "📋", "weight": 1.2},
    {"id": "bases_legales", "label": "Bases légales",                "icon": "⚖️", "weight": 1.3},
    {"id": "droits",        "label": "Droits des personnes",         "icon": "🙋", "weight": 1.2},
    {"id": "securite",      "label": "Sécurité des données",        "icon": "🔒", "weight": 1.5},
    {"id": "sous_traitants","label": "Sous-traitants & Transferts",  "icon": "🤝", "weight": 1.1},
    {"id": "violations",    "label": "Violations de données",        "icon": "🚨", "weight": 1.0},
]

QUESTIONS = [
    # --- Gouvernance ---
    {
        "id": "g1", "category": "gouvernance",
        "text": "Un responsable de la protection des données (DPO ou référent RGPD) est-il désigné au sein de votre entreprise ?",
        "options": [
            {"value": 2, "label": "Oui, un DPO désigné officiellement"},
            {"value": 1, "label": "Oui, un référent interne informel"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Désignez un référent RGPD (ou DPO si obligatoire) chargé de piloter la conformité. Ce point est critique pour structurer votre démarche.",
        "priority": "haute",
    },
    {
        "id": "g2", "category": "gouvernance",
        "text": "Vos collaborateurs ont-ils reçu une formation ou une sensibilisation au RGPD ?",
        "options": [
            {"value": 2, "label": "Oui, formation formelle régulière"},
            {"value": 1, "label": "Oui, sensibilisation ponctuelle"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Organisez au minimum une sensibilisation annuelle sur les bonnes pratiques RGPD (phishing, gestion des mots de passe, signalement d'incidents).",
        "priority": "moyenne",
    },
    {
        "id": "g3", "category": "gouvernance",
        "text": "Disposez-vous d'une politique interne de protection des données formalisée ?",
        "options": [
            {"value": 2, "label": "Oui, document écrit et diffusé"},
            {"value": 1, "label": "En cours de rédaction"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Rédigez une charte ou politique interne de protection des données et rendez-la accessible à tous les collaborateurs.",
        "priority": "moyenne",
    },

    # --- Registre ---
    {
        "id": "r1", "category": "registre",
        "text": "Tenez-vous un registre des activités de traitement (Article 30 RGPD) ?",
        "options": [
            {"value": 2, "label": "Oui, registre complet et à jour"},
            {"value": 1, "label": "Registre partiel ou non mis à jour"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Le registre des traitements est obligatoire. Cartographiez tous vos traitements : finalité, catégories de données, durées de conservation, destinataires.",
        "priority": "haute",
    },
    {
        "id": "r2", "category": "registre",
        "text": "Avez-vous défini des durées de conservation pour chaque catégorie de données personnelles ?",
        "options": [
            {"value": 2, "label": "Oui, durées documentées et appliquées"},
            {"value": 1, "label": "Partiellement défini"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Définissez des durées de conservation pour chaque traitement et mettez en place des procédures d'archivage/suppression automatiques.",
        "priority": "haute",
    },
    {
        "id": "r3", "category": "registre",
        "text": "Réalisez-vous des Analyses d'Impact (AIPD/DPIA) pour les traitements à risque élevé ?",
        "options": [
            {"value": 2, "label": "Oui, systématiquement"},
            {"value": 1, "label": "Ponctuellement"},
            {"value": 0, "label": "Non / Ne sais pas"},
        ],
        "recommendation": "Identifiez les traitements à risque élevé (profilage, données sensibles, surveillance) et réalisez une AIPD avant leur mise en œuvre.",
        "priority": "moyenne",
    },

    # --- Bases légales ---
    {
        "id": "bl1", "category": "bases_legales",
        "text": "Avez-vous identifié la base légale (consentement, contrat, obligation légale, intérêt légitime…) pour chacun de vos traitements ?",
        "options": [
            {"value": 2, "label": "Oui, pour tous les traitements"},
            {"value": 1, "label": "Pour la plupart des traitements"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Chaque traitement doit reposer sur une base légale valide. Documentez-la dans votre registre pour chaque activité.",
        "priority": "haute",
    },
    {
        "id": "bl2", "category": "bases_legales",
        "text": "Lorsque vous recueillez le consentement, est-il libre, spécifique, éclairé et univoque ?",
        "options": [
            {"value": 2, "label": "Oui, cases à cocher non pré-cochées, granulaire"},
            {"value": 1, "label": "Partiellement (mention groupée ou vague)"},
            {"value": 0, "label": "Non / Non applicable"},
        ],
        "recommendation": "Revoyez vos formulaires de collecte : le consentement doit être actif (case non pré-cochée), spécifique à chaque finalité et facilement retirable.",
        "priority": "haute",
    },
    {
        "id": "bl3", "category": "bases_legales",
        "text": "Envoyez-vous des emails marketing ? Si oui, disposez-vous d'un opt-in conforme ?",
        "options": [
            {"value": 2, "label": "Oui, opt-in explicite + désinscription facile"},
            {"value": 1, "label": "Opt-in approximatif ou opt-out uniquement"},
            {"value": 0, "label": "Non applicable"},
        ],
        "recommendation": "Pour le marketing, le consentement préalable explicite est requis (opt-in). Chaque email doit proposer un lien de désinscription fonctionnel.",
        "priority": "moyenne",
    },

    # --- Droits ---
    {
        "id": "d1", "category": "droits",
        "text": "Vos mentions légales / politique de confidentialité informent-elles les personnes de leurs droits ?",
        "options": [
            {"value": 2, "label": "Oui, complète et accessible"},
            {"value": 1, "label": "Incomplète ou difficile à trouver"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Rédigez une politique de confidentialité claire (identité du responsable, finalités, durées, droits, contact DPO) affichée sur votre site et vos formulaires.",
        "priority": "haute",
    },
    {
        "id": "d2", "category": "droits",
        "text": "Avez-vous mis en place une procédure pour répondre aux demandes d'exercice des droits (accès, rectification, suppression...) dans un délai d'1 mois ?",
        "options": [
            {"value": 2, "label": "Oui, procédure écrite et opérationnelle"},
            {"value": 1, "label": "Informellement géré"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Définissez un processus interne : qui reçoit les demandes, qui les traite, dans quel délai. Documenter les réponses apportées.",
        "priority": "haute",
    },
    {
        "id": "d3", "category": "droits",
        "text": "Disposez-vous d'un contact dédié (email ou formulaire) pour les demandes RGPD des personnes concernées ?",
        "options": [
            {"value": 2, "label": "Oui, clairement identifié et fonctionnel"},
            {"value": 1, "label": "Un email générique est utilisé"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Publiez une adresse email dédiée (ex: rgpd@votreentreprise.fr) sur votre site et dans vos documents contractuels.",
        "priority": "moyenne",
    },

    # --- Sécurité ---
    {
        "id": "s1", "category": "securite",
        "text": "Vos données personnelles sont-elles chiffrées (au repos et en transit) ?",
        "options": [
            {"value": 2, "label": "Oui, chiffrement complet (HTTPS, chiffrement BDD)"},
            {"value": 1, "label": "Partiellement (HTTPS uniquement)"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Activez HTTPS (TLS 1.2+) sur tous vos services, chiffrez les bases de données contenant des données personnelles et les sauvegardes.",
        "priority": "haute",
    },
    {
        "id": "s2", "category": "securite",
        "text": "Appliquez-vous le principe du moindre privilège (accès restreints selon le rôle) ?",
        "options": [
            {"value": 2, "label": "Oui, gestion des droits par rôle"},
            {"value": 1, "label": "Partiellement"},
            {"value": 0, "label": "Non, accès larges par défaut"},
        ],
        "recommendation": "Mettez en place une gestion des accès basée sur les rôles (RBAC) : chaque collaborateur n'accède qu'aux données nécessaires à sa mission.",
        "priority": "haute",
    },
    {
        "id": "s3", "category": "securite",
        "text": "Réalisez-vous des sauvegardes régulières et testez-vous leur restauration ?",
        "options": [
            {"value": 2, "label": "Oui, sauvegardes automatiques + tests réguliers"},
            {"value": 1, "label": "Sauvegardes sans tests"},
            {"value": 0, "label": "Non ou rare"},
        ],
        "recommendation": "Mettez en place des sauvegardes automatiques quotidiennes (ou plus fréquentes), stockées hors site, et testez leur restauration au moins 2 fois par an.",
        "priority": "haute",
    },
    {
        "id": "s4", "category": "securite",
        "text": "Utilisez-vous des mots de passe forts et une authentification à deux facteurs (2FA) pour les accès sensibles ?",
        "options": [
            {"value": 2, "label": "Oui, 2FA activé + gestionnaire de mots de passe"},
            {"value": 1, "label": "Mots de passe complexes sans 2FA"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Déployez la 2FA sur tous les accès sensibles (messagerie, ERP, cloud). Utilisez un gestionnaire de mots de passe en entreprise.",
        "priority": "haute",
    },

    # --- Sous-traitants ---
    {
        "id": "st1", "category": "sous_traitants",
        "text": "Avez-vous signé des Accords de Traitement des Données (DPA) avec tous vos sous-traitants traitant des données personnelles ?",
        "options": [
            {"value": 2, "label": "Oui, tous les sous-traitants couverts"},
            {"value": 1, "label": "Pour certains sous-traitants seulement"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Concluez un DPA (Data Processing Agreement - Art. 28 RGPD) avec chaque prestataire qui traite des données pour votre compte (hébergeur, CRM, comptable...).",
        "priority": "haute",
    },
    {
        "id": "st2", "category": "sous_traitants",
        "text": "Avez-vous vérifié que vos sous-traitants clés sont conformes au RGPD ?",
        "options": [
            {"value": 2, "label": "Oui, vérification documentée (audit, certifications)"},
            {"value": 1, "label": "Vérification informelle"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Évaluez régulièrement la conformité de vos sous-traitants principaux : demandez leur documentation RGPD, certifications ISO 27001, etc.",
        "priority": "moyenne",
    },
    {
        "id": "st3", "category": "sous_traitants",
        "text": "Utilisez-vous des services cloud basés hors UE (ex: AWS USA, Google, Microsoft) ? Si oui, des garanties de transfert sont-elles en place (SCC, décision d'adéquation) ?",
        "options": [
            {"value": 2, "label": "Oui, garanties formelles en place"},
            {"value": 1, "label": "Incertain / en cours de vérification"},
            {"value": 0, "label": "Non, aucune garantie identifiée"},
        ],
        "recommendation": "Vérifiez que vos fournisseurs extra-UE utilisent les Clauses Contractuelles Types (CCT) de la Commission européenne ou bénéficient d'une décision d'adéquation.",
        "priority": "moyenne",
    },

    # --- Violations ---
    {
        "id": "v1", "category": "violations",
        "text": "Disposez-vous d'une procédure de gestion des violations de données (notification CNIL sous 72h) ?",
        "options": [
            {"value": 2, "label": "Oui, procédure écrite et testée"},
            {"value": 1, "label": "Procédure informelle"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Rédigez une procédure de gestion des incidents : détection, qualification, notification CNIL (72h), notification aux personnes si risque élevé, documentation.",
        "priority": "haute",
    },
    {
        "id": "v2", "category": "violations",
        "text": "Tenez-vous un registre des violations de données (même mineures) ?",
        "options": [
            {"value": 2, "label": "Oui, registre tenu à jour"},
            {"value": 1, "label": "Partiellement"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Maintenez un registre interne de toutes les violations (y compris celles ne nécessitant pas de notification CNIL) : date, nature, impact, mesures prises.",
        "priority": "moyenne",
    },
    {
        "id": "v3", "category": "violations",
        "text": "Vos collaborateurs savent-ils à qui signaler un incident de sécurité ou une fuite de données ?",
        "options": [
            {"value": 2, "label": "Oui, canal de signalement clair et connu"},
            {"value": 1, "label": "Vaguement"},
            {"value": 0, "label": "Non"},
        ],
        "recommendation": "Communiquez clairement le canal de signalement (email dédié, référent RGPD) et sensibilisez régulièrement sur les exemples d'incidents à signaler.",
        "priority": "moyenne",
    },
]
