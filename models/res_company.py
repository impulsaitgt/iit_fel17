from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.company'

    fel_emisor_codigo = fields.Char(string='Emisor Codigo')
    fel_emisor_clave = fields.Char(string='Emisor Clave')
    fel_url_nit = fields.Char(string='Url Nit')
    fel_entorno = fields.Selection([ ('P','Produccion'),('D','Desarrollo/Pruebas')],string='Entorno',required=True, default='D')
    fel_codigo_imp = fields.Selection([ ('S','Si'),('N','No')],string='Imprime codigo al final',required=True, default='N')

    fel_UsuarioFirma = fields.Char(string='Usuario Firma (Prefijo WS)')
    fel_LlaveFirma = fields.Char(string='Llave Firma (Token Signer)')
    fel_UsuarioApi = fields.Char(string='Usuario Api  (Prefijo WS)')
    fel_LlaveApi = fields.Char(string='Llave Api (Llave WS)')
    fel_service = fields.Selection([ ('S','Si'),('N','No')],string='Usa Web Service',required=True, default='N')
    fel_url = fields.Char(string='URL para visualizacion')
    fel_codigo_establecimiento = fields.Char(string='Codigo Establecimiento')
    fel_correo_emisor = fields.Char(string='Correo Emisor')
    fel_nit_emisor = fields.Char(string='NIT Emisor')
    fel_nombre_Comercial = fields.Char(string='Nombre Comercial')
    fel_nombre_emisor = fields.Char(string='Nombre Emisor')
    fel_url_firma = fields.Char(string='Url Firma')
    fel_direccion = fields.Char(string='Direccion')
    fel_codigo_postal = fields.Char(string="Codigo Postal")
    fel_departamento = fields.Char(string="Departamento")
    fel_municipio = fields.Char(string='Municipio')

    fel_frases = fields.One2many(comodel_name='fel.res.partner.frases', inverse_name='fel_res_partner_id')


class ResPartnerFrases(models.Model):
    _name = 'fel.res.partner.frases'

    fel_res_partner_id = fields.Many2one(comodel_name='res.company')
    fel_frases_tipos = fields.Char(string="Documentos relacionados", required=True, default="FACT")
    fel_frases_codigo_escenario = fields.Char(string="Codigo Escenario", required=True)
    fel_frases_tipo_frase = fields.Char(string="Tipo Frase", required=True)


