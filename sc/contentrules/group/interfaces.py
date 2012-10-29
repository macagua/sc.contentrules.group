# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.schema import Choice
from zope.schema import Set
from zope.schema import TextLine

from sc.contentrules.group import MessageFactory as _


class IGroupAction(Interface):
    """An action used to create a group
    """

    groupid = TextLine(title=_(u"Group Id"),
                       description=_(u"Please inform the id for the user"
                                     u"group to be created by this action."
                                     u"Use  ${title} in this field to use "
                                     u"the content title in the Group Id."),
                       required=True)

    grouptitle = TextLine(title=_(u"Group title"),
                          description=_(u"Please inform the title for the user"
                                        u" group to be created by this action."
                                        u"Use ${title} in here to have the "
                                        u"content title in the Group Title."),
                          required=False)

    roles = Set(title=_(u"Roles"),
                description=_(u"Global roles to be assigned to the"
                              u"user group created by this action."),
                required=True,
                value_type=Choice(vocabulary='plone.app.vocabularies.Roles'))
