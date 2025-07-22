from compas_fea2.base import FEAData


class _Constraint(FEAData):
    """Base class for constraints.

    A constraint removes degree of freedom of nodes in the model.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def __data__(self):
        return {
            "class": self.__class__.__base__.__name__,
        }

    @classmethod
    def __from_data__(cls, data):
        return cls(**data)


# ------------------------------------------------------------------------------
# MPC
# ------------------------------------------------------------------------------


class _MultiPointConstraint(_Constraint):
    """A MultiPointConstraint (MPC) links a node (master) to other nodes (slaves) in the model.

    Parameters
    ----------
    constraint_type : str
        Type of the constraint.
    master : :class:`compas_fea2.model.Node`
        Node that acts as master.
    slaves : List[:class:`compas_fea2.model.Node`] | :class:`compas_fea2.model.NodesGroup`
        List or Group of nodes that act as slaves.
    tol : float
        Constraint tolerance, distance limit between master and slaves.

    Attributes
    ----------
    constraint_type : str
        Type of the constraint.
    master : :class:`compas_fea2.model.Node`
        Node that acts as master.
    slaves : List[:class:`compas_fea2.model.Node`] | :class:`compas_fea2.model.NodesGroup`
        List or Group of nodes that act as slaves.
    tol : float
        Constraint tolerance, distance limit between master and slaves.

    Notes
    -----
    Constraints are registered to a :class:`compas_fea2.model.Model`.

    """

    def __init__(self, constraint_type: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.constraint_type = constraint_type

    @property
    def __data__(self):
        data = super().__data__
        data.update(
            {
                "constraint_type": self.constraint_type,
                # ...other attributes...
            }
        )
        return data

    @classmethod
    def __from_data__(cls, data):
        return cls(constraint_type=data["constraint_type"], **data)


class TieMPC(_MultiPointConstraint):
    """Tie MPC that constraints axial translations."""


class BeamMPC(_MultiPointConstraint):
    """Beam MPC that constraints axial translations and rotations."""


# TODO check!
class _SurfaceConstraint(_Constraint):
    """A SurfaceConstraint links a surface (master) to another surface (slave) in the model.

    Parameters
    ----------
    master : :class:`compas_fea2.model.Node`
        Node that acts as master.
    slaves : List[:class:`compas_fea2.model.Node`] | :class:`compas_fea2.model.NodesGroup`
        List or Group of nodes that act as slaves.
    tol : float
        Constraint tolerance, distance limit between master and slaves.

    Attributes
    ----------
    master : :class:`compas_fea2.model.Node`
        Node that acts as master.
    slaves : List[:class:`compas_fea2.model.Node`] | :class:`compas_fea2.model.NodesGroup`
        List or Group of nodes that act as slaves.
    tol : float
        Constraint tolerance, distance limit between master and slaves.

    """

    @property
    def __data__(self):
        data = super().__data__
        # ...update data with specific attributes...
        return data

    @classmethod
    def __from_data__(cls, data):
        return cls(**data)

class FixConstraint(_Constraint):
    """Fixed constraint"""


class TieConstraint(_SurfaceConstraint):
    """Tie constraint between two surfaces."""
