#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable
def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para la campaña de Kéfir Plus.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("¿Dónde puedo comprar este producto?")
        # tema = 'Preguntas sobre el Producto'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario en un tema específico basado en patrones regex.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Comparación con Kéfir Casero/Artesanal
        # (Prioridad alta - es un tema muy recurrente)
        if re.search(
            r'b[úu]lgaros|n[oó]dulos|en casa|casero|artesanal|'
            r'preparo yo|hago mi|preparo mi|vendo el cultivo|hecho por mi|'
            r'hago yo|mejor hacer|tengo b[úu]lgaros|regalo.*b[úu]lgaros|'
            r'f[aá]cil.*hacer|c[oó]mo.*prepara|tu mism[ao]',
            comment_lower
        ):
            return 'Comparación con Kéfir Casero/Artesanal'
        
        # CATEGORÍA 2: Precio y Valor Percibido
        # (Nueva categoría - muy mencionado en comentarios)
        if re.search(
            r'\bcaro\b|muy caro|tan caro|absurdamente caro|precio|'
            r'econ[oó]mic[oa]|vale|cuesta|m[aá]s barato|'
            r'dejando pobre|paladar de pobre|sale m[aá]s',
            comment_lower
        ):
            return 'Precio y Valor Percibido'
        
        # CATEGORÍA 3: Ingredientes y Composición
        if re.search(
            r'conservantes|colorantes|saborizantes|aditivos|'
            r'almid[oó]n|preservantes|qu[ií]micos|azúcar|az[uú]car|'
            r'gelatina|procesad[oa]|industrial|c[aá]ncer|cero qu[ií]mico|'
            r'fructuosa|natural|libre de',
            comment_lower
        ):
            return 'Ingredientes y Composición'
        
        # CATEGORÍA 4: Beneficios de Salud y Experiencias
        if re.search(
            r'microbiota|flora intestinal|probi[oó]tic|digestión|'
            r'gastritis|helicobacter|pylori|col[oó]n|irritable|'
            r'cur[eé]|me cur[oó]|bueno para|ayuda|salud|'
            r'intolerante.*lactosa|lactosa|sin lactosa|'
            r'fermentaci[oó]n|bacterias',
            comment_lower
        ):
            return 'Beneficios de Salud y Experiencias'
        
        # CATEGORÍA 5: Sabor y Experiencia de Consumo
        if re.search(
            r'sabe feo|sabe refeo|no me asent[oó]|rico|delicioso|'
            r'no me gusta|me encanta|sabor|paladar|'
            r'diarrea|me dio|mala experiencia',
            comment_lower
        ):
            return 'Sabor y Experiencia de Consumo'
        
        # CATEGORÍA 6: Competencia y Marcas Alternativas
        if re.search(
            r'dejamu|pomar|san mart[ií]n|colanta|'
            r'mejor el de|otro|marca|alternativa|'
            r'd1|ara|tienda',
            comment_lower
        ):
            return 'Competencia y Marcas Alternativas'
        
        # CATEGORÍA 7: Disponibilidad y Distribución
        if re.search(
            r'no ha llegado|no lo encuentro|yopal|dónde|d[oó]nde|'
            r'donde comprar|consigo|disponible|venden|'
            r'no hay|difícil conseguir|cliente',
            comment_lower
        ):
            return 'Disponibilidad y Distribución'
        
        # CATEGORÍA 8: Recetas y Usos
        if re.search(
            r'receta|ch[ií]a|avena|granola|c[oó]mo.*prepara|'
            r'combino con|mezclo|preparar',
            comment_lower
        ):
            return 'Recetas y Usos'
        
        # CATEGORÍA 9: Comentarios sobre la Publicidad/Influencer
        if re.search(
            r'caitlyn jenner|kardashian|pilates|mewing|'
            r'doctor[a]|pupi|cata|divina|publicidad|'
            r'marketing|publicit|sponsor',
            comment_lower
        ):
            return 'Comentarios sobre la Publicidad'
        
        # CATEGORÍA 10: Fuera de Tema / Solo Emojis
        # Detectar comentarios que son principalmente emojis o muy cortos
        emoji_count = len(re.findall(r'[😀-🙏🌀-🗿]|❤️|♥️|✨|💛|💗|💞|💋|🌺|🌹|👍|🙊|🙏', comment))
        word_count = len([w for w in comment_lower.split() if len(w) > 2])
        
        if emoji_count > word_count or word_count < 2:
            return 'Fuera de Tema / Solo Emojis'
        
        if re.search(
            r'^\s*\[sticker\]\s*$|^xd$|^jaja|^gracias$|'
            r'^bendiciones$|^am[eé]n$|^si$|^no$|'
            r'^❤|^♥|^✨',
            comment_lower.strip()
        ):
            return 'Fuera de Tema / Solo Emojis'
        
        # CATEGORÍA 11: Otros
        return 'Otros'
    
    return classify_topic
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
